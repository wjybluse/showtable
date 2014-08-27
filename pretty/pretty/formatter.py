__author__ = 'wan'


class Formatter():
    def __init__(self, message, func=None, filtes=dict()):
        self.message = message
        self.func = func
        self.filters = filtes

    def create(self):
        pass

    @property
    def show(self):
        pass

    @property
    def clear(self):
        pass