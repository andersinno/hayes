# -*- coding: utf-8 -*-
import logging

from six import string_types

from hayes.indexing import CompletionSuggestField, DocumentIndex
from hayes.search import Search, SearchResults
from hayes.search.queries import Query, QueryStringQuery
from hayes.transport import BadRequestError, ESSession, NotFoundError
from hayes.utils import batch_iterable, object_to_dict


class CompletionSuggestionResults(object):
    def __init__(self, index, raw_result):
        self.index = index
        self.raw_result = raw_result
        self.options = raw_result.get("options") or ()


class Hayes(object):
    def __init__(self, server, default_coll_name=None):
        self.log = logging.getLogger("Hayes")
        if "://" not in server:
            server = "http://%s/" % server
        self.session = ESSession(base_url=server)
        self.default_coll_name = default_coll_name

    def index_objects(self, index, objects_iterable,
                      bulk_size, coll_name=None):
        coll_name = coll_name or self.default_coll_name
        if not coll_name:
            raise ValueError("No coll_name given")
        doctype = index.name
        keys = set(index.fields)
        keys.update(("id", "_id"))

        n = 0
        if not bulk_size or bulk_size <= 0:
            for obj in objects_iterable:
                obj = object_to_dict(obj, keys=keys)
                obj_id = obj.pop("_id", None) or obj.pop("id", None)
                if obj_id is not None:
                    self.session.put("/%s/%s/%s" %
                                     (coll_name, doctype, obj_id), data=obj)
                else:
                    self.session.post("/%s/%s/" %
                                      (coll_name, doctype), data=obj)
                n += 1
        else:
            for obj_batch in batch_iterable(objects_iterable, bulk_size):
                batch = []
                for obj in obj_batch:
                    obj = object_to_dict(obj, keys=keys)
                    obj_id = obj.pop("_id", None) or obj.pop("id", None)
                    if obj_id is not None:
                        batch.append(({"index": {"_id": obj_id}}, obj))
                    else:
                        batch.append(({"index": {}}, obj))
                resp = self.session.bulk(
                    "post", "/%s/%s/_bulk" % (coll_name, doctype),
                    data=batch).json()
                n += len(resp.get("items") or ())
        return n

    def rebuild_index(self, index, delete_first=True, coll_name=None):
        assert isinstance(index, DocumentIndex)
        coll_name = coll_name or self.default_coll_name
        doctype = index.name

        settings = index.get_settings_fragment()
        try:
            # Create the collection
            self.session.put("/%s/" % coll_name, data=settings)
        except BadRequestError as exc:
            if "IndexAlreadyExistsException" in exc.message:
                # Already existed, thus close, update settings, reopen (bleeeh)
                self.session.post("/%s/_close" % coll_name)
                self.session.put("/%s/_settings" % coll_name, data=settings)
                self.session.post("/%s/_open" % coll_name)
            else:
                raise  # We didn't expect _this_ exception

        if delete_first:
            try:
                self.session.delete("/%s/%s" % (coll_name, doctype))
                self.log.info("Mapping %s deleted.", doctype)
            except NotFoundError:
                pass
        self.session.put("/%s/%s/_mapping" %
                         (coll_name, doctype), data=index.get_mapping())

    def completion_suggest(self, index, text, fuzzy=None, coll_name=None):
        coll_name = coll_name or self.default_coll_name
        doctype = index.name
        key = "%s-sugg" % doctype

        try:
            completion_suggest_field_name = [
                name
                for (name, f)
                in index.fields.items()
                if isinstance(f, CompletionSuggestField)
            ][0]
        except IndexError:
            raise ValueError("Index doesn't have a CompletionSuggestField")
        sugg_doc = {"text": text, "completion": {
            "field": completion_suggest_field_name}}
        if fuzzy:
            sugg_doc["completion"]["fuzzy"] = {"unicode_aware": True}

        data = self.session.post("/%s/_suggest" %
                                 coll_name, data={key: sugg_doc}).json()
        return CompletionSuggestionResults(index, data[key][0])

    def search(self, search, indexes=None, count=50,
               start=0, page=None, coll_name=None):
        coll_name = coll_name or self.default_coll_name

        if isinstance(
                search, string_types):  # This is a silly default, I suppose
            search = Search(QueryStringQuery(search))
        if isinstance(search, Query):
            search = Search(query=search)

        search_obj = object_to_dict(search)
        if indexes:
            url = "/%s/%s/_search" % (coll_name,
                                      ",".join(i.name for i in indexes))
        else:
            url = "/%s/_search" % coll_name

        search_obj["from"] = int(start)
        search_obj["size"] = int(count)
        if page is not None:
            search_obj["from"] = search_obj["size"] * page

        data = self.session.get(url, data=search_obj).json()
        return SearchResults(search=search, raw_result=data,
                             start=start, count=count)

    def search_iter(self, search, indexes=None,
                    count=50, start=0, coll_name=None):
        while True:
            res = self.search(search=search, indexes=indexes,
                              count=count, start=start, coll_name=coll_name)
            if not res.hits:
                break
            for hit in res.hits:
                yield hit
            start += count
