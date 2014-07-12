__author__ = 'wan'
import unittest
from restserver.http_server import HTTPServer
from restserver.https_server import HTTPSServer

def get_header():
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    headers["Content-length"] = 0
    #headers["Authorizon"] = "Basic %s" % (base64.encodebytes
    return headers

class TestHTTPserver(unittest.TestCase):
    def test_send_mesage_success(self):
        server=HTTPServer("127.0.0.1",3000)
        self.assertRegex(server._get_response("get","/blog/show/1",None,header=get_header()),"errorReason")

if __name__=="__main__":
    unittest.main()
