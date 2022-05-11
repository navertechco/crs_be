from .libs import *


def secure_method(func):
    def inner(*args, **kwargs):
        token = request.headers.get('token')
        if token is None:
            return ErrorResponse(MAINTENANCE)
        if token != TOKEN:
            return ErrorResponse(MAINTENANCE)
        returned_value = func(*args, **kwargs)
        return returned_value
    inner.__name__ = func.__name__
    return inner
