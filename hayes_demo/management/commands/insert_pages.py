# -*- coding: utf-8 -*-
import bz2
import json

from django.core.management import BaseCommand
from django.db.transaction import commit_on_success

from hayes_test.models import Page


class Command(BaseCommand):
    @commit_on_success
    def handle(self, filename="", **kwargs):
        if filename.endswith(".xml"):
            generator = self.parse_xml(filename)
        elif filename.endswith(".json.bz2"):
            with bz2.BZ2File(filename) as in_f:
                data = json.load(in_f, encoding="UTF-8")
            generator = data
        else:
            print(
                ("filename given: %r, can only read .xml (wikipedia abstracts)"
                 " or .json.bz2 (prepared abstracts)") % filename)
            return

        for entry in generator:
            if Page.objects.filter(url=entry["url"]).exists():
                continue
            Page.objects.create(**entry)
            print "Created: %r" % entry["url"]

    def parse_xml(self, filename):
        from lxml import etree
        with file(filename, "rb") as fp:
            for event, element in etree.iterparse(fp):
                if event == "end" and element.tag == "doc":
                    try:
                        title = element.find("title").text.replace(
                            "Wikipedia: ", "")
                    except BaseException:
                        continue

                    try:
                        abstract = element.find("abstract").text
                    except BaseException:
                        continue

                    try:
                        url = element.find("url").text
                    except BaseException:
                        continue

                    if len(title) < 5:
                        continue
                    if not abstract:
                        continue
                    if "|" in abstract:
                        continue
                    if abstract.startswith("=="):
                        continue
                    if len(abstract) < 50:
                        continue

                    data = {"title": title, "url": url, "abstract": abstract}
                    yield data
