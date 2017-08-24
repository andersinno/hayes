# -*- coding: utf-8 -*-
import hashlib
import random

from faker import Factory

from hayes.analysis import SnowballAnalyzer, StandardAnalyzer
from hayes.indexing import (
    CompletionSuggestField, DateField, DocumentIndex, IntegerField,
    StringField, TextField)
from hayes_demo.models import Page


class Person(dict):
    def __init__(self, locale, id):
        super(Person, self).__init__()
        fake = Factory.create(locale)
        fake.seed(hash(hashlib.sha1("%s,%s" % (locale, id)).hexdigest()))
        self["id"] = id
        self["name"] = fake.name()
        self["street"] = fake.street_address()
        self["city"] = fake.city().lower().title()
        self["description"] = fake.text(max_nb_chars=150)
        self["locale"] = locale
        self["birth_date"] = fake.date_time_this_decade()
        self["height"] = random.randint(140, 190)


standard_analyzer = StandardAnalyzer("std")


class PeopleIndex(DocumentIndex):
    def __init__(self, locale):
        self.locale = locale
        self.name = "people:%s" % locale
        self.fields = {
            "name": TextField(analyzer=standard_analyzer),
            "street": TextField(analyzer=standard_analyzer),
            "city": TextField(analyzer=standard_analyzer),
            "description": TextField(
                analyzer=SnowballAnalyzer(name="en", language="English")),
            "locale": StringField(),
            "birth_date": DateField(),
            "height": IntegerField(),
        }

    def get_objects(self):
        for id in range(50):
            object = Person(locale=self.locale, id=id)
            yield dict(object)


class PageIndex(DocumentIndex):
    name = "pages"
    fi_analyzer = SnowballAnalyzer(name="fi", language="Finnish")
    fields = {
        "suggest": CompletionSuggestField(
            index_analyzer=fi_analyzer,
            search_analyzer=fi_analyzer,
            preserve_separators=False,
            payloads=True
        ),
        "title": TextField(fi_analyzer, boost=2),
        "abstract": TextField(fi_analyzer),
        "url": StringField(),
        "_all": TextField(fi_analyzer),
    }

    def get_model(self):
        return Page

    def get_object(self, page):
        doc = {"_id": page.pk, "title": page.title,
               "url": page.url, "abstract": page.abstract}
        doc["suggest"] = {
            "input": doc["title"],
            "output": doc["title"],
            "payload": {"url": doc["url"]}
        }
        return doc

    def get_objects(self):
        for page in Page.objects.iterator():
            doc = self.get_object(page)
            yield doc


def get_indexes():
    for locale in ("en_US", "it_IT", "fr_FR"):
        yield PeopleIndex(locale)
    yield PageIndex()
