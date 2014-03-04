# -- encoding: UTF-8 --
from itertools import islice
import logging
from pprint import pprint

from hayes.indexing import DocumentIndex, CompletionSuggestField
from hayes.search import Search, SearchResults
from hayes.search.queries import QueryStringQuery, Query
from hayes.transport import ESSession, BadRequestError, NotFoundError
from hayes.utils import object_to_dict


class CompletionSuggestionResults(object):
	def __init__(self, index, raw_result):
		self.index = index
		self.raw_result = raw_result
		self.options = raw_result.get("options") or ()


class Hayes(object):
	def __init__(self, server, index):
		self.log = logging.getLogger("Hayes")
		if not server.startswith("http://"):
			server = "http://%s/" % server
		self.session = ESSession(base_url=server)
		self.index = index

	def index_objects(self, index, objects_iterable, bulk_size):
		coll_name = self.index
		doctype = index.name
		keys = set(index.fields)
		keys.update(("id", "_id"))

		n = 0
		if not bulk_size or bulk_size <= 0:
			for obj in objects_iterable:
				obj = object_to_dict(obj, keys=keys)
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
					obj = object_to_dict(obj, keys=keys)
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
		coll_name = self.index
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
		coll_name = self.index
		doctype = index.name
		key = "%s-sugg" % doctype

		try:
			completion_suggest_field_name = [name for (name, f) in index.fields.iteritems() if isinstance(f, CompletionSuggestField)][0]
		except IndexError:
			raise ValueError("Index doesn't have a CompletionSuggestField")
		sugg_doc = {"text": text, "completion": {"field": completion_suggest_field_name}}
		if fuzzy:
			sugg_doc["completion"]["fuzzy"] = {"unicode_aware": True}

		data = self.session.post("/%s/_suggest" % (coll_name), data={key: sugg_doc}).json()
		return CompletionSuggestionResults(index, data[key][0])

	def search(self, search, indexes=None, count=50, start=0, page=None):
		if isinstance(search, basestring):  # This is a silly default, I suppose
			search = Search(QueryStringQuery(search))
		if isinstance(search, Query):
			search = Search(query=search)

		search_obj = object_to_dict(search)
		if indexes:
			url = "/%s/%s/_search" % (self.index, ",".join(i.name for i in indexes))
		else:
			url = "/%s/_search" % (self.index)

		search_obj["from"] = int(start)
		search_obj["size"] = int(count)
		if page is not None:
			search_obj["from"] = search_obj["size"] * page

		pprint(search_obj)

		data = self.session.get(url, data=search_obj).json()
		return SearchResults(search=search, raw_result=data, start=start, count=count)
