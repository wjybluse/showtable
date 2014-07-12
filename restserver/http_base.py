__author__ = 'wan'
import json
class HTTPScheme():
    def __init__(self,host,port):
        self.host=host
        self.port=port
    def _get_response(self,meth,uri,body,header={}):
        pass

    def parse_json(self,e):
        return json.dumps({"errorReason":str(e)})

    def parse_rsp(self,rsp):
        return json.dumps(rsp)
