# -- encoding: UTF-8 --

from django.conf import settings
from hayes.importing import load
from hayes.indexing import DocumentIndex


def get_configured_indexes():
	for index_spec in getattr(settings, "HAYES_INDEXES", ()):
		if not callable(index_spec):
			index_spec = load(index_spec)
		result = index_spec()
		if isinstance(result, DocumentIndex):
			result = [result]
		for index in result:
			yield index
