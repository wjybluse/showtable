__author__ = 'wan'
import unittest

from restserver.http_server import HTTPServer
from restserver.https_server import HTTPSServer


def get_header():
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    #headers["Authorizon"] = "Basic %s" % (base64.encodebytes
    return headers

class TestHTTPserver(unittest.TestCase):
    def test_send_mesage_failed(self):
        server = HTTPServer("127.0.0.1", 6000)
        self.assertRegex(server._get_response("GET", "/blog/show/1", body=None, header=get_header()), "errorReason")

    def test_send_message_success(self):
        server=HTTPServer("127.0.0.1",3000)
        value = server._get_response("GET", "/blog/show/1", body=None, header=get_header())
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_https_send_failed(self):
        server = HTTPSServer("127.0.0.1", 3000)
        self.assertRegex(server._get_response("GET", "/blog/show/1", None, header=get_header()), "errorReason")

    def test_https_send_success(self):
        server = HTTPSServer("127.0.0.1", 5000)
        value = server._get_response("PUT", "/blog/show/1", body='{"dsads":"dsadsa"}', header=get_header())
        print(value)
        self.assertNotRegex(value, "errorReason")


if __name__=="__main__":
    unittest.main()
