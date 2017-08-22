# -*- coding: utf-8 -*-
from six import iteritems, text_type

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
    for key, value in iteritems(in_dict):
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
        return {"query_string": {"query": text_type(self.query)}}


class MatchQuery(Query):
    def __init__(self, field, value, operator=None, fuzziness=None):
        self.field = field
        self.value = value
        self.operator = operator
        self.fuzziness = fuzziness

    def as_dict(self):
        query_frag = {self.field: {"query": text_type(self.value)}}
        if self.operator is None:
            return {"match": query_frag}
        if self.operator in ("or", "and"):
            query_frag["operator"] = self.operator
        elif self.operator in ("phrase", "phrase_prefix"):
            query_frag["type"] = self.operator
        if self.fuzziness:
            query_frag["fuzziness"] = self.fuzziness

        return {"match": query_frag}


class BoolQuery(Query):
    def __init__(self, must=None, must_not=None, should=None,
                 boost=None, minimum_should_match=None):
        self.must = must
        self.must_not = must_not
        self.should = should
        self.boost = boost
        self.minimum_should_match = minimum_should_match

    def as_dict(self):
        out = {
            "must": ([object_to_dict(d) for d in self.must]
                     if self.must else None),
            "must_not": ([object_to_dict(d) for d in self.must_not]
                         if self.must_not else None),
            "should": ([object_to_dict(d) for d in self.should]
                       if self.should else None),
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
        return _clean_dict({
            "prefix": {
                self.field: {
                    "value": self.value,
                    "boost": float(self.boost) if self.boost else None
                }
            }
        })


class TermQuery(Query):
    def __init__(self, field, value, boost=None):
        self.field = field
        self.value = value
        self.boost = boost

    def as_dict(self):
        return _clean_dict({
            "term": {
                self.field: {
                    "value": text_type(self.value),
                    "boost": self.boost
                }
            }
        })


class WildcardQuery(Query):
    def __init__(self, field, value, boost=None):
        self.field = field
        self.value = value
        self.boost = boost

    def as_dict(self):
        return _clean_dict({
            "wildcard": {
                self.field: {
                    "value": text_type(self.value),
                    "boost": self.boost
                }
            }
        })


class FuzzyQuery(Query):
    def __init__(self, field, value, boost=None, fuzziness=2,
                 prefix_length=0, max_expansions=100):
        self.field = field
        self.value = value
        self.boost = boost
        self.fuzziness = fuzziness
        self.prefix_length = prefix_length
        self.max_expansions = max_expansions

    def as_dict(self):
        return _clean_dict({
            "fuzzy": {
                self.field: {
                    "value": text_type(self.value),
                    "boost": self.boost,
                    "fuzziness": self.fuzziness,
                    "prefix_length": self.prefix_length,
                    "max_expansions": self.max_expansions
                }
            }
        })
