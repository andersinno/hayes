# -*- coding: utf-8 -*-
from hayes import Hayes
from hayes_tests.utils import MockSession
import pytest


@pytest.fixture
def hayes():
    h = Hayes("http://127.0.0.2:9999")
    h.session = MockSession("http://127.0.0.2:9999")
    return h
