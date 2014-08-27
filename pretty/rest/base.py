__author__ = 'wan'
from pretty.tools.utils import *


class HTTPScheme():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def response(self, method, uri, body=None, headers={}, func=None):
        try:
            self._client.request(method, uri, body, headers)
            rsp = self._client.getresponse()
            msg = rsp.read()
            if msg is None or len(msg) <= 0:
                return good_response_without_message()
            return message_with_func(msg.encode('utf-8'), func)
        except Exception as e:
            return bad_response(e)
        finally:
            self._client.close()

    @property
    def _client(self):
        pass
