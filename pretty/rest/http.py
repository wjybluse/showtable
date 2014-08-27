__author__ = 'wan'

from httplib import HTTPConnection

import base


class HTTPClient(base.HTTPScheme):
    def __init__(self, host, port):
        base.HTTPScheme.__init__(self, host, port)

    def _client(self):
        return HTTPConnection(self.host, self.port)






