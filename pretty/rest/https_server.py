__author__ = 'wan'
from http import client

from pretty.rest.restserver.http_base import HTTPScheme


class HTTPSServer(HTTPScheme):
    def __init__(self, host, port):
        HTTPScheme.__init__(self, host, port)

    def _get_response(self, meth, uri, body=None, header={}, fun=None):
        conn = client.HTTPSConnection(self.host, port=self.port, timeout=2 * 60 * 1000, key_file=None, cert_file=None)
        try:
            conn.request(meth, uri, body, header)
            data = conn.getresponse().read()
            if data is None or len(data) <= 0:
                return self.default_ok_message()
            return self.parse_rsp(data.decode("utf-8"), fun)
        except Exception as e:
            return self.parse_json(e)
        finally:
            conn.close()

