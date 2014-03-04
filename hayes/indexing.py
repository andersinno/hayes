# -- encoding: UTF-8 --

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


class SearchField(object):
	store = False
	def as_dict(self):
		return {}


class StringField(SearchField):
	def as_dict(self):
		return {"type": "string", "index": "not_analyzed", "store": self.store}


class TextField(StringField):
	def __init__(self, analysis="basic", **kwargs):
		self.analysis = analysis

	def as_dict(self):
		return {"type": "string", "index": "analyzed", "store": self.store}  # XXX -- analysis


class BaseNumberField(SearchField):
	pass


class IntegerField(BaseNumberField):
	def as_dict(self):
		return {"type": "integer", "store": self.store}


class DecimalField(BaseNumberField):
	def as_dict(self):
		return {"type": "double", "store": self.store}


class DateField(SearchField):
	def as_dict(self):
		return {"type": "date", "store": self.store}

class BooleanField(SearchField):
	def as_dict(self):
		return {"type": "boolean", "store": self.store}
