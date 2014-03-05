# -- encoding: UTF-8 --
from django.core.management import BaseCommand
from hayes.django_interop import get_connection, get_configured_indexes


class Command(BaseCommand):
	def handle(self, *args, **options):
		conn = get_connection()
		for index in get_configured_indexes():
			print "Working on index", index.name
			conn.rebuild_index(index)
			conn.index_objects(index, index.get_objects(), bulk_size=300)
