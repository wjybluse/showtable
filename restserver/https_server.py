__author__ = 'wan'
from http import client

from restserver.http_base import HTTPScheme


class HTTPSServer(HTTPScheme):
    def __init__(self, host, port):
        HTTPScheme.__init__(self, host, port)

    def _get_response(self, meth, uri, body=None, header={}):
        print("method is %s,uri is %s ,body is %s,header is %s" % (meth, uri, body, header))
        conn = client.HTTPSConnection(self.host, port=self.port, timeout=2 * 60 * 1000, key_file=None, cert_file=None)
        try:
            conn.request(meth, uri, body, header)
            return self.parse_rsp(conn.getresponse().read().decode("utf-8"))
        except Exception as e:
            return self.parse_json(e)
        finally:
            conn.close()

