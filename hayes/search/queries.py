# -- encoding: UTF-8 --
from hayes.search.filters import AndFilter
from hayes.utils import object_to_dict


class Query(object):
	pass


class QueryStringQuery(object):
	def __init__(self, query):
		self.query = query

	def as_dict(self):
		return {"query_string": {"query": unicode(self.query)}}

class MatchQuery(object):
	def __init__(self, field, value, operator="and"):
		self.field = field
		self.value = value
		self.operator = operator

	def as_dict(self):
		if self.operator in ("or", "and"):
			return {"match": ({self.field: {"query": unicode(self.value), "operator": self.operator}})}
		elif self.operator == "phrase":
			return {"match": ({self.field: {"query": unicode(self.value), "type": "phrase"}})}
		elif self.operator == "phrase_prefix":
			return {"match": ({self.field: {"query": unicode(self.value), "type": "phrase_prefix"}})}

class BoolQuery(object):
	def __init__(self, must=None, must_not=None, should=None, boost=1.0, minimum_should_match=None):
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
		out = dict((k, v) for (k, v) in out.iteritems() if v is not None)
		return {"bool": out}

class RangeQuery(object):
	def __init__(self):
		self.ranges = {}

	def add_range(self, field, gte=None, gt=None, lte=None, lt=None, boost=1.0):
		out = {}
		if gte:
			out["gte"] = gte
		elif gt:
			out["gt"] = gt

		if lte:
			out["lte"] = lte
		elif lt:
			out["lt"] = lt

		if out:
			out["boost"] = float(boost)
			self.ranges[field] = out

	def as_dict(self):
		return {"range": self.ranges}


class FilteredQuery(object):
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
