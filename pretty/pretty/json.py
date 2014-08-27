__author__ = 'wan'
import formatter


class PrettyJson():
    def __init__(self, message, func=None, filtes=dict()):
        formatter.Formatter.__init__(message, func, filtes)

    def create(self):
        pass

    def show(self):
        pass