__author__ = 'wan'
from http import client

from restserver.http_base import HTTPScheme


class HTTPServer(HTTPScheme):
    def __init__(self,host,port):
        HTTPScheme.__init__(self,host,port)

    def _get_response(self, meth, uri, body=None, header={}):
        print("method is %s,uri is %s ,body is %s,header is %s" % (meth, uri, body, header))
        conn = client.HTTPConnection(self.host, port=self.port)
        try:
            conn.request(meth,uri,body,header)
            rsp=conn.getresponse()
            msg = rsp.read().decode("utf-8")
            return self.parse_rsp(msg)
        except Exception as e:
            print("error reason is %s" % (e))
            return self.parse_json(e)
        finally:
            conn.close()





