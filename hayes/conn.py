# -- encoding: UTF-8 --
from itertools import islice
import json
import datetime
import logging
import requests
from requests.exceptions import HTTPError
from hayes.indexing import DocumentIndex, CompletionSuggestField


def to_dict(obj, keys=None):
	out = {}

	if isinstance(obj, dict):
		if not keys:
			return obj
		src = obj
	else:
		src = vars(obj)

	return dict((k, v) for (k, v) in src.iteritems() if ((not keys or k in keys) and not k.startswith("__") and not callable(v)))


def json_encode(object):
	if isinstance(object, datetime.datetime):
		return object.isoformat()
	else:
		raise ValueError("Can't encode %r" % object)


class NotFoundError(HTTPError):
	pass


class BadRequestError(HTTPError):
	pass

class ForbiddenError(HTTPError):
	pass


class ESSession(requests.Session):
	def __init__(self, base_url):
		super(ESSession, self).__init__()
		self.base_url = base_url

	def request(self, method, url, **kwargs):
		if url.startswith("/"):
			url = self.base_url + url
		data = kwargs.pop("data", None)
		if data and isinstance(data, dict):
			data = json.dumps(data, default=json_encode)

		kwargs.update(method=method, url=url, data=data)

		resp = super(ESSession, self).request(**kwargs)
		if resp.status_code == 404:
			raise NotFoundError(resp.json()["error"], response=resp)
		elif resp.status_code == 400:
			raise BadRequestError(resp.json()["error"], response=resp)
		elif resp.status_code == 403:
			raise ForbiddenError(resp.json()["error"], response=resp)
		resp.raise_for_status()
		return resp

	def bulk(self, method, url, data, **kwargs):
		batch = []
		for command, payload in data:
			batch.append(command)
			batch.append(payload)
		data = "\n".join(json.dumps(obj, default=json_encode) for obj in batch) + "\n"
		return self.request(method, url, data=data, **kwargs)

class Hayes(object):
	def __init__(self, server, default_index):
		self.log = logging.getLogger("Hayes")
		if not server.startswith("http://"):
			server = "http://%s/" % server
		self.session = ESSession(base_url=server)
		self.default_index = default_index

	def index_objects(self, index, objects_iterable, bulk_size):
		coll_name = index.index or self.default_index
		doctype = index.name
		keys = set(index.fields)
		keys.update(("id", "_id"))

		n = 0
		if not bulk_size or bulk_size <= 0:
			for obj in objects_iterable:
				obj = to_dict(obj, keys=keys)
				id = obj.pop("_id", None) or obj.pop("id", None)
				if id is not None:
					self.session.put("/%s/%s/%s" % (coll_name, doctype, id), data=obj)
				else:
					self.session.post("/%s/%s/" % (coll_name, doctype), data=obj)
				n += 1
		else:
			while True:
				batch = []
				for obj in islice(objects_iterable, 0, bulk_size):
					obj = to_dict(obj, keys=keys)
					id = obj.pop("_id", None) or obj.pop("id", None)
					if id is not None:
						batch.append(({"index": {"_id": id}}, obj))
					else:
						batch.append(({"index": {}}, obj))
				if not batch:
					break
				resp = self.session.bulk("post", "/%s/%s/_bulk" % (coll_name, doctype), data=batch).json()

				n += len(resp.get("items") or ())
		return n

	def rebuild_index(self, index, bulk_size=0, delete_first=True):
		assert isinstance(index, DocumentIndex)
		coll_name = index.index or self.default_index
		doctype = index.name

		settings = index.get_settings_fragment()
		try:
			self.session.put("/%s/" % coll_name, data=settings)  # Create the collection
		except BadRequestError:  # Already existed, thus close, update settings, reopen (bleeeh)
			self.session.post("/%s/_close" % coll_name)
			self.session.put("/%s/_settings" % coll_name, data=settings)
			self.session.post("/%s/_open" % coll_name)

		if delete_first:
			try:
				self.session.delete("/%s/%s" % (coll_name, doctype))
				self.log.info("Mapping %s deleted." % doctype)
			except NotFoundError:
				pass
		self.session.put("/%s/%s/_mapping" % (coll_name, doctype), data={"properties": index.get_mapping()})


		return self.index_objects(index, index.get_objects(), bulk_size=bulk_size)

	def completion_suggest(self, index, text, fuzzy=None):

		coll_name = index.index or self.default_index
		doctype = index.name
		key = "%s-sugg" % doctype

		try:
			completion_suggest_field_name = [name for (name, f) in index.fields.iteritems() if isinstance(f, CompletionSuggestField)][0]
		except IndexError:
			raise ValueError("Index doesn't have a CompletionSuggestField")
		sugg_doc = {"text": text, "completion": {"field": completion_suggest_field_name}}
		if fuzzy:
			sugg_doc["completion"]["fuzzy"] = {"unicode_aware": True}
		return self.session.post("/%s/_suggest" % (coll_name), data={key: sugg_doc}).json()
