# -*- coding: utf-8 -*-
from hayes.utils import object_to_dict


class _HighlightBaseSpec(object):
    def __init__(self, tag_schema=None, pre_tags=None, post_tags=None,
                 number_of_fragments=None, fragment_size=None,
                 order=None):
        self.tag_schema = tag_schema
        self.pre_tags = pre_tags
        self.post_tags = post_tags
        self.number_of_fragments = number_of_fragments
        self.fragment_size = fragment_size
        self.order = order

    def to_dict(self):
        out = {}
        if self.pre_tags is not None:
            out["pre_tags"] = list(self.pre_tags)
            out["post_tags"] = list(self.post_tags)
        elif self.tag_schema is not None:
            out["tag_schema"] = self.tag_schema

        if self.number_of_fragments is not None:
            out["number_of_fragments"] = int(self.number_of_fragments)
        if self.fragment_size is not None:
            out["fragment_size"] = int(self.fragment_size)
        if self.order is not None:
            out["order"] = self.order
        return out


class HighlightFieldSpec(_HighlightBaseSpec):
    pass


class HighlightSpec(_HighlightBaseSpec):
    def __init__(self, fields=None, **kwargs):
        super(HighlightSpec, self).__init__(**kwargs)
        self.fields = dict(fields or {})

    def to_dict(self):
        out = super(HighlightSpec, self).to_dict()
        out["fields"] = dict((name, object_to_dict(spec))
                             for (name, spec) in self.fields.items())
        return out
