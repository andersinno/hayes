# -- encoding: utf-8 --
from __future__ import with_statement
import sys
from django.conf import settings

#from hayes.models import DjangoElasticSearchModel, DjangoResultSet

from hayes.conn import Hayes


# def get_haystack_ct(model):
# 	return "%s.%s" % (model._meta.app_label, model._meta.module_name)
#
#
# class DumpWrite(object):
# 	def write(self, string):
# 		print >>sys.stderr, string
#
# class Hayes(object):
# 	@classmethod
# 	def from_haystack(cls, connection="default"):
# 		connection = settings.HAYSTACK_CONNECTIONS[connection]
# 		url = connection["URL"]
# 		index_name = connection["INDEX_NAME"]
# 		return cls(index_name=index_name, server=url)
#
# 	def __init__(self, index_name, server=None, dump=False):
# 		if dump:
# 			dump = DumpWrite()
# 		else:
# 			dump = None
#
# 		self.es = ES(server=server or "localhost:9200", dump_curl=dump)
# 		self.index_name = index_name
# 		self.models = {}
#
# 	def _get_es_model(self, django_model):
# 		es_model = self.models.get(django_model)
# 		if not es_model:
# 			base = DjangoElasticSearchModel
# 			es_model = type("%s%s" % (django_model.__name__, base.__name__), (base,), {"django_model": django_model})
# 			self.models[django_model] = es_model
# 		return es_model
#
# 	def search(self, models, query, default_field="text", field_filters={}, result_fields=()):
# 		ct_map = dict((model, get_haystack_ct(model)) for model in models)
# 		es_model_map = dict((ct_map[model], self._get_es_model(model)) for model in models)
#
# 		def get_model(connection, data):
# 			if not data:
# 				return None
# 			ct = data.get("id", data.get("_id")).rsplit(".", 1)[0]
# 			return es_model_map[ct](connection, data)
#
# 		filters = [
# 			TermFilter("django_ct", sorted(ct_map.values()))
# 		]
#
# 		for field, value in field_filters.iteritems():
# 			filters.append(TermFilter(field, value))
#
# 		filter = BoolFilter(must=filters)
# 		query = StringQuery(query, default_field=default_field, analyze_wildcard=True)
# 		query = FilteredQuery(query, filter)
# 		search = Search(query, fields=(result_fields or None), size=50)
# 		return DjangoResultSet(
# 			connection=self.es,
# 			search=search,
# 			indices=[self.index_name],
# 			doc_types=["modelresult"],
# 			model=get_model,
# 			query_params={}
# 		)
#
# 	def analyze(self, text, analyzer=None):
# 		return self.es.indices.analyze(text, index=self.index_name, analyzer=analyzer)
