__author__ = 'wan'
import formatter


class PrettyXML():
    def __init__(self, message, func=None, filtes=dict()):
        formatter.Formatter.__init__(message, func, filtes)

    def show(self):
        pass

    def create(self):
        pass