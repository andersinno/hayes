# -*- coding: utf-8 -*-
import pytest

from hayes import Hayes

from .utils import MockSession


@pytest.fixture
def hayes():
    h = Hayes("http://127.0.0.2:9999")
    h.session = MockSession("http://127.0.0.2:9999")
    return h
