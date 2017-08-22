# -*- coding: utf-8 -*-

import datetime
import json

import requests
from requests.exceptions import HTTPError


def json_encode(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    else:
        raise ValueError("Can't encode %r" % (obj,))


class NotFoundError(HTTPError):
    pass


class BadRequestError(HTTPError):
    pass


class ForbiddenError(HTTPError):
    pass


class ESSession(requests.Session):
    def __init__(self, base_url):
        super(ESSession, self).__init__()
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        if url.startswith("/"):
            url = self.base_url + url
        data = kwargs.pop("data", None)
        if data and isinstance(data, dict):
            data = json.dumps(data, default=json_encode)

        kwargs.update(method=method, url=url, data=data)

        resp = super(ESSession, self).request(**kwargs)
        error_message = resp.json().get("error", "")
        if resp.status_code == 404:
            raise NotFoundError(error_message, response=resp)
        elif resp.status_code == 400:
            raise BadRequestError(error_message, response=resp)
        elif resp.status_code == 403:
            raise ForbiddenError(error_message, response=resp)
        resp.raise_for_status()
        return resp

    def bulk(self, method, url, data, **kwargs):
        batch = []
        for command, payload in data:
            batch.append(command)
            batch.append(payload)
        data = "\n".join(json.dumps(obj, default=json_encode)
                         for obj in batch) + "\n"
        return self.request(method, url, data=data, **kwargs)
