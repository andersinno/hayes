# -*- coding: utf-8 -*-
from hayes.analysis import AnalysisBase, builtin_simple_analyzer
from hayes.utils import object_to_dict


class DocumentIndex(object):
    name = None
    fields = {}
    enable_source = True
    enable_size = False
    enable_timestamp = False

    def get_model(self):  # For Django compat.
        return None

    def get_objects(self):
        return ()

    def get_mapping(self):
        mapping_json = {}
        mapping_json["_source"] = {"enabled": self.enable_source}
        if self.enable_size:
            mapping_json["_size"] = {
                "enabled": True, "store": True, "type": "int"}
        if self.enable_size:
            mapping_json["_timestamp"] = {
                "enabled": True, "store": True, "type": "date"}

        properties = mapping_json["properties"] = {}

        for field_name, field in self.fields.items():
            if field_name == "_all":
                mapping_json["_all"] = object_to_dict(field)
            else:
                assert isinstance(field, SearchField)
                properties[field_name] = object_to_dict(field)

        return mapping_json

    def get_analysis_settings_fragment(self):
        analyzers_by_name = {}
        tokenizers_by_name = {}
        filters_by_name = {}
        for field in self.fields.values():
            if hasattr(field, "get_analyzers"):  # It could be a dict too
                for analyzer in field.get_analyzers():
                    if analyzer and isinstance(analyzer, AnalysisBase):
                        analyzers_by_name[analyzer.name] = analyzer
                        filters_by_name.update(
                            (f.name, f)
                            for f in getattr(analyzer, "filters", ())
                            if hasattr(f, "name"))
                        tokenizer = getattr(analyzer, "tokenizer", None)
                        if getattr(tokenizer, "name", None):
                            tokenizers_by_name[tokenizer.name] = tokenizer

        def to_dict_m(m):
            out = {}
            for k in m.values():
                d = k.to_dict()
                if d:
                    out[k.name] = d
            return out

        return {
            "analyzer": to_dict_m(analyzers_by_name),
            "tokenizer": to_dict_m(tokenizers_by_name),
            "filter": to_dict_m(filters_by_name),
        }

    def get_settings_fragment(self):
        return {
            "index": {
                "analysis": self.get_analysis_settings_fragment()
            }
        }


class SearchField(object):
    stored = False
    indexed = True

    def as_dict(self):
        return {}

    def get_analyzers(self):
        return filter(None, [
            getattr(self, "analyzer", None),
            getattr(self, "index_analyzer", None),
            getattr(self, "search_analyzer", None),
        ])


class StringField(SearchField):
    def __init__(self, boost=1.0):
        self.boost = boost

    def as_dict(self):
        return {
            "type": "string",
            "index": ("not_analyzed" if self.indexed else "none"),
            "store": self.stored,
            "boost": self.boost
        }


class TextField(StringField):
    def __init__(self, analyzer=None, boost=1.0, term_vector="no"):
        super(TextField, self).__init__(boost=boost)
        self.analyzer = analyzer
        self.term_vector = term_vector
        if self.term_vector not in (
                "no", "yes", "with_offsets", "with_positions",
                "with_positions_offsets"):
            raise ValueError("What a strange 'term_vector' value")

    def as_dict(self):
        val = {
            "type": "string",
            "index": ("analyzed" if self.indexed else "none"),
            "store": self.stored,
            "boost": self.boost,
            "term_vector": self.term_vector
        }
        if self.analyzer:
            val["analyzer"] = self.analyzer.name
        return val


class BaseNumberField(SearchField):
    pass


class IntegerField(BaseNumberField):
    def as_dict(self):
        return {"type": "integer", "store": self.stored}


class DecimalField(BaseNumberField):
    def as_dict(self):
        return {"type": "double", "store": self.stored}


class DateField(SearchField):
    def as_dict(self):
        return {"type": "date", "store": self.stored}


class BooleanField(SearchField):
    def as_dict(self):
        return {"type": "boolean", "store": self.stored}


class CompletionSuggestField(SearchField):
    stored = False

    def __init__(self, index_analyzer=builtin_simple_analyzer,
                 search_analyzer=builtin_simple_analyzer, payloads=False,
                 preserve_separators=True):
        self.index_analyzer = index_analyzer
        self.search_analyzer = search_analyzer
        self.payloads = bool(payloads)
        self.preserve_separators = bool(preserve_separators)

    def as_dict(self):
        return {
            "type": "completion",
            "payloads": self.payloads,
            "preserve_separators": self.preserve_separators,
            "index_analyzer": self.index_analyzer.name,
            "search_analyzer": self.search_analyzer.name,
        }
