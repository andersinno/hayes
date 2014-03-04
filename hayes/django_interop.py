# -- encoding: UTF-8 --

from django.conf import settings
from hayes.conn import Hayes
from hayes.importing import load
from hayes.indexing import DocumentIndex

_indexes_cache = None

def _get_configured_indexes():
	for index_spec in getattr(settings, "HAYES_INDEXES", ()):
		if not callable(index_spec):
			index_spec = load(index_spec)
		result = index_spec()
		if isinstance(result, DocumentIndex):
			result = [result]
		for index in result:
			yield index


def get_configured_indexes():
	global _indexes_cache
	if _indexes_cache is None:
		_indexes_cache = list(_get_configured_indexes())
	return _indexes_cache


def get_connection():
	return Hayes(server=settings.HAYES_SERVER, default_index=settings.HAYES_DEFAULT_INDEX)
