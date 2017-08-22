# -*- coding: utf-8 -*-
from requests.models import Response

from hayes.transport import ESSession


class MockSession(ESSession):
    def send(self, request, **kwargs):
        resp = Response()
        resp.status_code = 200
        resp._content = b"{}"
        return resp
