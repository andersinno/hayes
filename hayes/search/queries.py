# -- encoding: UTF-8 --
from hayes.search.filters import AndFilter
from hayes.search.internal import _Ranges
from hayes.utils import object_to_dict

def _clean_dict(in_dict):
	"""
	Recursively remove None-valued items from dict.
	:param in_dict:
	:return:
	"""
	out = {}
	for key, value in in_dict.iteritems():
		if isinstance(value, dict):
			value = _clean_dict(value)
		if value is None:
			continue
		out[key] = value
	return out

class Query(object):
	pass


class QueryStringQuery(Query):
	def __init__(self, query):
		self.query = query

	def as_dict(self):
		return {"query_string": {"query": unicode(self.query)}}


class MatchQuery(Query):
	def __init__(self, field, value, operator=None):
		self.field = field
		self.value = value
		self.operator = operator

	def as_dict(self):
		if self.operator is None:
			return {"match": ({self.field: unicode(self.value)})}
		elif self.operator in ("or", "and"):
			return {"match": ({self.field: {"query": unicode(self.value), "operator": self.operator}})}
		elif self.operator == "phrase":
			return {"match": ({self.field: {"query": unicode(self.value), "type": "phrase"}})}
		elif self.operator == "phrase_prefix":
			return {"match": ({self.field: {"query": unicode(self.value), "type": "phrase_prefix"}})}


class BoolQuery(Query):
	def __init__(self, must=None, must_not=None, should=None, boost=None, minimum_should_match=None):
		self.must = must
		self.must_not = must_not
		self.should = should
		self.boost = boost
		self.minimum_should_match = minimum_should_match

	def as_dict(self):
		out = {
			"must": [object_to_dict(d) for d in self.must] if self.must else None,
			"must_not": [object_to_dict(d) for d in self.must_not] if self.must_not else None,
			"should": [object_to_dict(d) for d in self.should] if self.should else None,
		    "boost": self.boost,
		    "minimum_should_match": self.minimum_should_match
		}
		return {"bool": _clean_dict(out)}


class RangeQuery(_Ranges, Query):
	def as_dict(self):
		return {"range": self.ranges}


class FilteredQuery(Query):
	def __init__(self, query, filter):
		self.query = query
		if isinstance(filter, (tuple, list)):
			filter = AndFilter(filters=list(filter))
		self.filter = filter

	def as_dict(self):
		return {
			"filtered": {
				"query": object_to_dict(self.query),
				"filter": object_to_dict(self.filter)
			}
		}


class ConstantScoreQuery(Query):
	def __init__(self, filter):
		if isinstance(filter, (tuple, list)):
			filter = AndFilter(filters=list(filter))
		self.filter = filter

	def as_dict(self):
		return {
			"constant_score": {
				"filter": object_to_dict(self.filter)
			}
		}


class MatchAllQuery(Query):
	def as_dict(self):
		return {"match_all": {}}


class PrefixQuery(Query):
	def __init__(self, field, value, boost=None):
		self.field = field
		self.value = value
		self.boost = boost

	def as_dict(self):
		return _clean_dict({"prefix": {(self.field): {"value": self.value, "boost": float(self.boost) if self.boost else None}}})

class TermQuery(Query):
	def __init__(self, field, value, boost=None):
		self.field = field
		self.value = value
		self.boost = boost

	def as_dict(self):
		return _clean_dict({"term": {self.field: self.value, "boost": self.boost}})
