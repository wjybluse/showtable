__author__ = 'wan'
import json


class HTTPScheme():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _get_response(self, meth, uri, body=None, header={}, fun=None):
        pass

    def parse_json(self, e):
        return json.dumps({"errorReason": str(e)})

    def parse_rsp(self, rsp, fp=None):
        if fp is None:
            return json.dumps(rsp)
        else:
            return fp(rsp)

    def default_ok_message(self):
        return json.dump({"resultMsg": "ok"})
