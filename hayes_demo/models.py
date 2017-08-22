# -*- coding: utf-8 -*-

from django.db import models


class Page(models.Model):
	class Meta:
		db_table = 'pg'

	title = models.CharField(max_length=128)
	url = models.URLField(max_length=128, unique=True)
	abstract = models.TextField(blank=True)
