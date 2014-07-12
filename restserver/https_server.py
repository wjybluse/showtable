__author__ = 'wan'
from restserver.http_base import HTTPScheme
from http import client
class HTTPSServer(HTTPScheme):
    def __init__(self,host,port):
        HTTPScheme.__init__(self,host,port)

    def _get_response(self,meth,uri,body,header={}):
        conn=client.HTTPSConnection(self.host,port=self.port,timeout=2*60*1000,key_file=None,cert_file=None)
        try:
            conn.request(meth,uri,body,header)
            return self.parse_rsp(conn.getresponse().msg)
        except Exception as e:
            return self.parse_json(e)
        finally:
            conn.close()

