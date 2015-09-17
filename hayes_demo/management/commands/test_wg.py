# -- encoding: UTF-8 --
from django.core.management import BaseCommand

from hayes.django_interop import get_connection, get_index_by_name
from hayes.ext.word_gatherer import WordGatherer, smart_finnish_tokenizer


class Command(BaseCommand):
	def handle(self, *args, **options):
		conn = get_connection()
		index = get_index_by_name("pages")
		wg = WordGatherer(conn, "word-suggest")
		wg.reset()
		wg.update(index, ("abstract", "title"), tokenizer=smart_finnish_tokenizer)
		for x in wg.search("juna"):
			print x
