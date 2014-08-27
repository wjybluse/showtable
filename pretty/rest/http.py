__author__ = 'wan'
from http import client

from pretty.rest.server.http_base import HTTPScheme


class HTTPServer(HTTPScheme):
    def __init__(self, host, port):
        HTTPScheme.__init__(self, host, port)

    def _get_response(self, meth, uri, body=None, header={}, fun=None):
        conn = client.HTTPConnection(self.host, port=self.port)
        try:
            conn.request(meth, uri, body, header)
            rsp = conn.getresponse()
            msg = rsp.read()
            if msg is None or len(msg) <= 0:
                return self.default_ok_message()
            return self.parse_rsp(msg.decode("utf-8"), fp=fun)
        except Exception as e:
            print("error reason is %s" % (e))
            return self.parse_json(e)
        finally:
            conn.close()





