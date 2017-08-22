# -*- coding: utf-8 -*-

from six import text_type


class AnalysisBase(object):
    type = None

    def __init__(self, name):
        self.name = name

    def to_dict(self, **extra):
        d = {}
        if self.type:
            d["type"] = self.type
        d.update(extra)
        return d


class BuiltInAnalyzer(AnalysisBase):
    def to_dict(self, **extra):
        return None


class CustomAnalyzer(AnalysisBase):
    type = "custom"

    def __init__(self, name, tokenizer, filters):
        super(CustomAnalyzer, self).__init__(name=name)
        self.tokenizer = tokenizer
        self.filters = list(filters or [])

    def to_dict(self, **extra):
        filters = [text_type(getattr(f, "name", f)) for f in self.filters]
        return super(CustomAnalyzer, self).to_dict(
            tokenizer=self.tokenizer, filter=filters)


class StandardAnalyzer(AnalysisBase):
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


class SimpleAnalyzer(AnalysisBase):
    type = "simple"


class LanguageAnalyzer(AnalysisBase):
    KNOWN_LANGUAGES = (
        "arabic", "armenian", "basque", "brazilian", "bulgarian",
        "catalan", "chinese", "cjk", "czech", "danish", "dutch",
        "english", "finnish", "french", "galician", "german",
        "greek", "hindi", "hungarian", "indonesian", "italian",
        "norwegian", "persian", "portuguese", "romanian", "russian",
        "spanish", "swedish", "turkish", "thai",
    )

    def __init__(self, name, language="english"):
        super(LanguageAnalyzer, self).__init__(name)
        if language not in self.KNOWN_LANGUAGES:
            raise ValueError("Don't know about %r" % language)
        self.type = language


class SnowballAnalyzer(AnalysisBase):
    type = "snowball"
    KNOWN_LANGUAGES = (
        "Armenian", "Basque", "Catalan", "Danish", "Dutch", "English",
        "Finnish", "French", "German", "German2", "Hungarian",
        "Italian", "Kp", "Lovins", "Norwegian", "Porter", "Portuguese",
        "Romanian", "Russian", "Spanish", "Swedish", "Turkish",
    )

    def __init__(self, name, language="English"):
        super(SnowballAnalyzer, self).__init__(name)
        if language not in self.KNOWN_LANGUAGES:
            raise ValueError("Don't know about %r" % language)
        self.language = language

    def to_dict(self, **extra):
        return super(SnowballAnalyzer, self).to_dict(
            language=self.language, **extra)


class NgramTokenizer(AnalysisBase):
    type = "ngram"

    def __init__(self, name, min_gram=3, max_gram=8):
        super(NgramTokenizer, self).__init__(name)
        self.min_gram = min_gram
        self.max_gram = max_gram
        self.token_chars = ["letter"]

    def to_dict(self, **extra):
        return super(NgramTokenizer, self).to_dict(
            min_gram=self.min_gram,
            max_gram=self.max_gram,
            token_chars=self.token_chars,
            **extra
        )


####


class StopFilter(AnalysisBase):
    type = "stop"

    def __init__(self, name, stopwords):
        super(StopFilter, self).__init__(name)
        self.stopwords = stopwords

    def to_dict(self, **extra):
        return super(StopFilter, self).to_dict(
            stopwords=self.stopwords, **extra)


class StemmerFilter(AnalysisBase):
    type = "stemmer"

    def __init__(self, name, stemmer_name):
        super(StemmerFilter, self).__init__(name)
        self.stemmer_name = stemmer_name

    def to_dict(self, **extra):
        return super(StemmerFilter, self).to_dict(
            name=self.stemmer_name, **extra)


###

builtin_simple_analyzer = BuiltInAnalyzer(name="simple")
