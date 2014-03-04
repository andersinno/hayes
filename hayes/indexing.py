# -- encoding: UTF-8 --
from hayes.analysis import Analyzer, builtin_simple_analyzer


class DocumentIndex(object):
	index = None
	name = None
	fields = {}
	enable_source = True
	enable_size = False
	enable_timestamp = False

	def get_objects(self):
		return ()

	def get_mapping(self):
		mapping_json = {}
		mapping_json["_source"] = {"enabled" : self.enable_source}
		if self.enable_size:
			mapping_json["_size"] = {"enabled" : True, "store": True, "type": "int"}
		if self.enable_size:
			mapping_json["_timestamp"] = {"enabled": True, "store": True, "type": "date"}

		for field_name, field in self.fields.iteritems():
			assert isinstance(field, SearchField)
			mapping_json[field_name] = m = field.as_dict()

		return mapping_json

	def get_analysis_settings_fragment(self):
		analyzers_by_name = {}
		tokenizers_by_name = {}
		filters_by_name = {}
		for field in self.fields.itervalues():
			for analyzer in field.get_analyzers():
				if analyzer and isinstance(analyzer, Analyzer):
					analyzers_by_name[analyzer.name] = analyzer
					filters_by_name.update((f.name, f) for f in getattr(analyzer, "filters", ()))
					tokenizer = getattr(analyzer, "tokenizer", None)
					if tokenizer:
						tokenizers_by_name[tokenizer.name] = tokenizer

		def to_dict_m(m):
			out = {}
			for k in m.itervalues():
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
		return {"type": "string", "index": ("not_analyzed" if self.indexed else "none"), "store": self.stored, "boost": self.boost}


class TextField(StringField):
	def __init__(self, analyzer=None, boost=1.0):
		super(TextField, self).__init__(boost=boost)
		self.analyzer = analyzer

	def as_dict(self):
		val = {
			"type": "string",
			"index": ("analyzed" if self.indexed else "none"),
			"store": self.stored,
		    "boost": self.boost,
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
	def __init__(self, index_analyzer=builtin_simple_analyzer, search_analyzer=builtin_simple_analyzer, payloads=False, preserve_separators=True):
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
