__author__ = 'wan'
import base64
from restserver.http_server import HTTPServer
from restserver.https_server import HTTPSServer


class RestClient():
    def __init__(self, scheme, host, port, url, body=None):
        """
        :param scheme:str  http or https
        :param host: str like 127.0.0.1 or localhost
        :param port: int default port is 80 when scheme is http or 443 when scheme is https
        :param url: str /blog/post/1
        :param body: the content of rest
        """
        if not body: body = dict()
        self.url = url
        self.body = body
        if not 'https' is scheme.lower():
            self.server = HTTPSServer(host, port)
        else:
            self.server = HTTPServer(host, port)
        self.add_dynamic_method(lambda meth: setattr(self, meth, self._send_message(meth)))

    def _send_message(self, meth):
        self.server._get_response(meth, self.url, self.body, self._get_header())

    def add_dynamic_method(self, fp):
        method = ["get", "post", "get", "put", "head", "patch"]
        for meth in method:
            fp(meth)

    def _get_header(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        headers["Content-length"] = len(self.body)
        headers["Authorizon"] = "Basic %s" % (base64.encodebytes(b'234324:hahhah'))
        return self.server.parse_rsp(headers)
