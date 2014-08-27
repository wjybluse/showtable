__author__ = 'wan'
import json

METHOD = ['get', 'patch', 'delete', 'put', 'post', 'head', 'options']


def bad_response(e):
    # static return bad message
    return '{"error":"{0}"}'.format(e)


def good_response_without_message():
    return '{"msg":"send message successfully"}'


def _good_response_with_message(message):
    if isinstance(message, dict):
        return json.dumps(message)
    try:
        return json.dumps(message)
    except ValueError:
        return '{"msg":"{0}"}'.format(message)


def message_with_func(message, func):
    if func is None:
        return _good_response_with_message(message)
    return func(message)


def add_method(func):
    if func is None:
        raise ValueError("The object doesn't support add method when binding method is None")
    return lambda this: (setattr(this, method, func(method.upper())) for method in METHOD)


def default_headers():
    headers = dict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    return headers


# for create pretty
def get_max_length(arr=list()):
    """
    :max_length : int the max length of value
    """
    if len(arr) <= 0:
        return 0

<< << << < HEAD
return len(str(max(arr, key=lambda item: len(str(item)))))
== == == =
return len(max(arr, key=lambda item: len(str(item))))
>> >> >> > origin / master


def titles():
    return ["Property", "Value"]


def create_line():
    pass


def create_row(value):
    pass