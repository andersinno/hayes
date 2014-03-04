Hayes
=====

Simpler Elasticsearch for Django.

Very much a work in progress.

May contain hot buttered soul.

Usage Example
-------------

```
from hayes import Hayes
from django.contrib.auth.models import User

def find_staff_matching(query):
	hayes = Hayes.from_haystack()  # "default" haystack configuration by default
	resultset = hayes.search([User], query, field_filters={"is_staff": True})
	for obj in resultset.get_objects():
		print obj  # User object
		print obj._score  # Its ES score
		print obj._es  # Its ES object
```