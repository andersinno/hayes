Hayes
=====

Simpler Elasticsearch for Django (using Haystack indexing).

Very much a work in progress.

May contain hot buttered soul.

Usage Example
-------------

Assuming you have indexed the Django User model using Haystack:

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