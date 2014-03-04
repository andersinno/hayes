# -- encoding: UTF-8 --

class Analyzer(object):
	type = None
	def __init__(self, name):
		self.name = name

	def to_dict(self, **extra):
		d = {}
		if self.type:
			d["type"] = self.type
		d.update(extra)
		return d

class BuiltInAnalyzer(Analyzer):
	def to_dict(self):
		return None

class CustomAnalyzer(Analyzer):
	type = "custom"
	def __init__(self, name, tokenizer, filters):
		super(CustomAnalyzer, self).__init__(name=name)
		self.tokenizer = tokenizer
		self.filters = list(filters or [])

class StandardAnalyzer(Analyzer):
	type = "standard"
	def __init__(self, name, stopwords=None, max_token_length=255):
		super(StandardAnalyzer, self).__init__(name)
		self.stopwords = stopwords
		self.max_token_length = max_token_length

	def to_dict(self, **extra):
		return super(StandardAnalyzer, self).to_dict(
			stopwords=self.stopwords,
			max_token_length=int(self.max_token_length),
		)

class SimpleAnalyzer(Analyzer):
	type = "simple"

class LanguageAnalyzer(Analyzer):
	KNOWN_LANGUAGES = ("arabic", "armenian", "basque", "brazilian", "bulgarian", "catalan", "chinese", "cjk", "czech", "danish", "dutch", "english", "finnish", "french", "galician", "german", "greek", "hindi", "hungarian", "indonesian", "italian", "norwegian", "persian", "portuguese", "romanian", "russian", "spanish", "swedish", "turkish", "thai")

	def __init__(self, name, language="english"):
		super(LanguageAnalyzer, self).__init__(name)
		if language not in self.KNOWN_LANGUAGES:
			raise ValueError("Don't know about %r" % language)
		self.type = language

class SnowballAnalyzer(Analyzer):
	type = "snowball"
	KNOWN_LANGUAGES = ("Armenian", "Basque", "Catalan", "Danish", "Dutch", "English", "Finnish", "French", "German", "German2", "Hungarian", "Italian", "Kp", "Lovins", "Norwegian", "Porter", "Portuguese", "Romanian", "Russian", "Spanish", "Swedish", "Turkish")

	def __init__(self, name, language="English"):
		super(SnowballAnalyzer, self).__init__(name)
		if language not in self.KNOWN_LANGUAGES:
			raise ValueError("Don't know about %r" % language)
		self.language = language

	def to_dict(self, **extra):
		return super(SnowballAnalyzer, self).to_dict(language=self.language, **extra)

builtin_simple_analyzer = BuiltInAnalyzer(name="simple")
