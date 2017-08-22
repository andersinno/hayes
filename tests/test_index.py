# -*- coding: utf-8 -*-

from hayes.indexing import DocumentIndex


class MyIndex(DocumentIndex):
    name = "test"


def test_index_bulk(hayes):
    i = MyIndex()
    hayes.index_objects(i, ({"a": "b"},), 1000, "test")
