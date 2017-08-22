# -*- coding: utf-8 -*-
from hayes.search.internal import _Ranges
from hayes.utils import object_to_dict


class Filter(object):
    pass


class _MultiTermFilter(Filter):
    _kind = None

    def __init__(self, **terms):
        self.terms = {}
        self.terms.update(terms)

    def as_dict(self):
        return {self._kind: self.terms}


class TermsFilter(_MultiTermFilter):
    _kind = "terms"


class PrefixFilter(_MultiTermFilter):
    _kind = "prefix"


class _CompoundFilter(Filter):
    _kind = None

    def __init__(self, filters):
        self.filters = filters

    def as_dict(self):
        return {self._kind: {"filters": [
            object_to_dict(f) for f in self.filters]}}


class AndFilter(_CompoundFilter):
    _kind = "and"


class OrFilter(_CompoundFilter):
    _kind = "or"


class RangeQuery(_Ranges, Filter):
    def as_dict(self):
        return {"range": self.ranges}
