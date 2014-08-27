__author__ = 'wan'

from httplib import HTTPSConnection

import base


class HTTPSClient(base.HTTPScheme):
    def __init__(self, host, port):
        base.HTTPScheme.__init__(self, host, port)

    @property
    def _client(self):
        return HTTPSConnection(self.host, self.port)

