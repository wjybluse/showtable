__author__ = 'wan'
from restserver.http_server import HTTPServer
from restserver.https_server import HTTPSServer


class RestClient():
    '''
    this class is a simple rest client,you can use it like this:
    client=RestClient("http","localhost",80)
    client.get()
    '''

    def __init__(self, scheme, host, port):
        """
        :param scheme:str  http or https
        :param host: str like 127.0.0.1 or localhost
        :param port: int default port is 80 when scheme is http or 443 when scheme is https
        """
        if 'https'.__eq__(scheme.lower()):
            self.server = HTTPSServer(host, port)
        else:
            self.server = HTTPServer(host, port)
        self.headers = self._headers()
        #dynamic bind the method for self
        self.add_dynamic_method(lambda meth: setattr(self, meth, self._send_message(meth.upper())))

    def _send_message(self, meth):
        def get_rsp(body=None, url="/"):
            return self.server._get_response(meth, url, body=body, header=self.headers)

        return get_rsp

    def add_dynamic_method(self, fp):
        [fp(meth) for meth in ["get", "post", "put", "head", "patch", "delete"]]


    def _headers(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        return headers

    def add_header(self, key=None, value=None):
        if key is None or value is None:
            return self
        self.headers[key] = value
        return self

    def add_headers(self, headers={}):
        if headers is None or len(headers) <= 0:
            return self
        self.headers.update(headers)
        print("headers is %s" % (self.headers))
        return self

    def remove_heaader(self, key=None):
        if key is None:
            return self
        if self.headers.__contains__(key):
            self.headers.pop(key)
        return self

