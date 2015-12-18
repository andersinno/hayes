# -- encoding: UTF-8 --

import datetime
import json

import requests
from hayes.excs import error_from_response


def json_encode(object):
    if isinstance(object, datetime.datetime):
        return object.isoformat()
    elif isinstance(object, datetime.date):
        return object.isoformat()
    else:
        raise ValueError("Can't encode %r" % object)


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
        exc = error_from_response(response=resp, request_data=kwargs)
        if exc:
            raise exc
        resp.raise_for_status()
        return resp

    def bulk(self, method, url, data, **kwargs):
        batch = []
        for command, payload in data:
            batch.append(command)
            batch.append(payload)
        data = "\n".join(json.dumps(obj, default=json_encode) for obj in batch) + "\n"
        return self.request(method, url, data=data, **kwargs)
