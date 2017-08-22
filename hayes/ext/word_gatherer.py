# -*- coding: utf-8 -*-
import hashlib
import unicodedata
from collections import Counter, defaultdict

from six import text_type

from hayes.analysis import builtin_simple_analyzer
from hayes.ext.stopwords import (
    english_stopwords, finnish_stopwords, russian_stopwords, swedish_stopwords,
    unicode_punctuation_chars)
from hayes.indexing import DocumentIndex, IntegerField, TextField
from hayes.search import Search
from hayes.search.queries import MatchAllQuery, PrefixQuery


def default_tokenizer(content):
    return content.split()


def smart_tokenizer(content, stopwords=()):
    words = text_type(content).split()
    words = [word.strip(unicode_punctuation_chars) for word in words]
    words = [word for word in words if len(
        word) > 3 and word.lower() not in stopwords]
    # Filter out full numbers
    words = [word for word in words if not word.isdigit()]
    return words


def smart_finnish_tokenizer(content):
    return smart_tokenizer(content, stopwords=finnish_stopwords)


def smart_swedish_tokenizer(content):
    return smart_tokenizer(content, stopwords=swedish_stopwords)


def smart_russian_tokenizer(content):
    return smart_tokenizer(content, stopwords=russian_stopwords)


def smart_english_tokenizer(content):
    return smart_tokenizer(content, stopwords=english_stopwords)


class WordGatherer(object):
    def __init__(self, connection, target_type, coll_name=None):
        """
        :type connection: hayes.conn.Hayes
        """
        self.connection = connection
        self.target_type = target_type
        self.target_coll_name = (
            coll_name or self.connection.default_coll_name)
        self.index = index = DocumentIndex()
        index.name = self.target_type
        index.fields = {
            "word": TextField(analyzer=builtin_simple_analyzer),
            "count": IntegerField(),
        }

    def reset(self):
        """ Reset target collection (rebuild index).
        """
        self.connection.rebuild_index(
            self.index, coll_name=self.target_coll_name)

    def _tokenize_documents(self, index, fields, tokenizer=default_tokenizer):
        search = Search(MatchAllQuery())
        for doc in self.connection.search_iter(
                search, indexes=[index], count=200):
            for field in fields:
                value = doc.get(field)
                if not value:
                    continue
                words = tokenizer(value)
                yield doc, words

    def _gather_words(self, index, fields, tokenizer=default_tokenizer):
        word_counts = Counter()
        for _doc, words in self._tokenize_documents(
                index, fields, tokenizer=tokenizer):
            if words:
                for word in words:
                    word_counts[word] += 1
        return word_counts

    def update(self, index, fields, tokenizer=default_tokenizer, cutoff=1):
        """
        Update (upsert) the wordgatherer collection.
        :param index: Source index.
        :param fields: Fields to read.
        :param tokenizer: Tokenizer callable. Should split unicode to words
        :param cutoff: Ignore words with less than this many occurrences.
        """
        counts_by_uid = defaultdict(Counter)
        for word, count in self._gather_words(
                index, fields, tokenizer=tokenizer).items():
            uid = hashlib.sha1(unicodedata.normalize(
                "NFKD", word.lower()).encode("UTF-8")).hexdigest()
            counts_by_uid[uid][word] += count

        for uid, word_to_count in counts_by_uid.items():
            word = word_to_count.most_common(1)[0][0]
            count = sum(word_to_count.values())
            if count <= cutoff:
                continue
            self.connection.session.post(
                "/%s/%s/%s/_update" % (self.target_coll_name,
                                       self.target_type, uid),
                data={
                    "script": "ctx._source.count += count",
                    "params": {"count": count},
                    "upsert": {"word": word, "count": count}
                })

    def search(self, word, limit=30):
        """
        Search for a word within the wordgatherer collection.
        :param word: Word to search for.
        :param limit: Maximum number of results to return.
        """
        search = Search(PrefixQuery("word", word), sort={"count": "desc"})
        for doc in self.connection.search(
                search, indexes=[self.index], count=limit):
            yield (doc["word"], doc["count"])
