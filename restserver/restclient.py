__author__ = 'wan'
from restserver.http_server import HTTPServer
from restserver.https_server import HTTPSServer


class RestClient():
    '''
    this class is a simple rest client,you can use it like this:
    client=RestClient("http","localhost",80,"/")
    client.get()
    '''

    def __init__(self, scheme, host, port):
        """
        :param scheme:str  http or https
        :param host: str like 127.0.0.1 or localhost
        :param port: int default port is 80 when scheme is http or 443 when scheme is https
        """
        if 'https'.__eq__(scheme.lower()):
            print("the request is https")
            self.server = HTTPSServer(host, port)
        else:
            self.server = HTTPServer(host, port)
        #dynamic bind the method for self
        self.add_dynamic_method(lambda meth: setattr(self, meth, self._send_message(meth.upper())))

    def _send_message(self, meth):
        def get_rsp(body=None,url="/"):
            return self.server._get_response(meth, url, body=body, header=self.headers)
        return get_rsp

    def add_dynamic_method(self, fp):
        method = ["get", "post", "put", "head", "patch"]
        for meth in method:
            fp(meth)

    @property
    def headers(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        return headers
