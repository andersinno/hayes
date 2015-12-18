# coding=utf-8
import six

__all__ = [
    "ESError",
    "NotFoundError",
    "BadRequestError",
    "ForbiddenError"
]


class ESError(Exception):
    def __init__(self, message, type=None, response=None, request_data=None):
        self.message = six.text_type(message)
        self.type = type
        self.response = response
        self.request_data = request_data
        super(ESError, self).__init__(self.message)

    @classmethod
    def from_response(cls, response, request_data=None):
        message = response.text
        type = None
        try:
            json_data = response.json()
        except ValueError:
            json_data = None

        if json_data:
            error_data = json_data.get("error")
            if error_data:
                message = error_data.get("reason")
                type = error_data.get("type")

        return cls(message=message, type=type, response=response, request_data=request_data)


class NotFoundError(ESError):
    pass


class BadRequestError(ESError):
    pass


class ForbiddenError(ESError):
    pass


def error_from_response(response, request_data=None):
    if response.status_code < 400:
        return None
    exc_class = {
        404: NotFoundError,
        400: BadRequestError,
        403: ForbiddenError,
    }.get(response.status_code, ESError)
    return exc_class.from_response(response, request_data)
