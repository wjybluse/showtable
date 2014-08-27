__author__ = 'wan'
from pretty.rest.http import HTTPClient
from pretty.rest.https import HTTPSClient
from pretty.tools.utils import *


class RestClient():
    """
    this class is a simple rest client,you can use it like this:
    client=RestClient("http","localhost",80)
    client.get()
    """

    def __init__(self, scheme="http", host="localhost", port=80):
        """
        :param scheme:str  http or https
        :param host: str like 127.0.0.1 or localhost
        :param port: int default port is 80 when scheme is http or 443 when scheme is https
        """
        if 'https'.__eq__(scheme.lower()):
            self.client = HTTPSClient(host, port)
        else:
            self.client = HTTPClient(host, port)
        self.headers = default_headers()
        add_method(self._send_message)(self)

    def _send_message(self, method):
        def response(body=None, url="/"):
            return self.client.response(method, url, body=body, headers=self.headers)

        return response

    def add_header(self, key=None, value=None):
        if key is None or value is None:
            return self
        self.headers[key] = value
        return self

    def add_headers(self, headers=dict()):
        if headers is None or len(headers) <= 0:
            return self
        self.headers.update(headers)
        return self

    def remove_header(self, key=None):
        if key is None:
            return self
        if self.headers.__contains__(key):
            self.headers.pop(key)
        return self

