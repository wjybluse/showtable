__author__ = 'wan'
from restserver.http_base import HTTPScheme
from http import client
class HTTPServer(HTTPScheme):
    def __init__(self,host,port):
        HTTPScheme.__init__(self,host,port)

    def _get_response(self,meth,uri,body,header={}):
        conn=client.HTTPConnection(self.host,self.port)
        try:
            conn.request(meth,uri,body,header)
            rsp=conn.getresponse()
            return self.parse_rsp(rsp.msg)
        except Exception as e:
            return self.parse_json(e)
        finally:
            conn.close()





