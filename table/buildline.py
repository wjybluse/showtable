__author__ = 'wan'
#default mark
MARK = '|'


class BuildLine():
    def __init__(self, mark):
        if mark is None:
            self.line = MARK
        else:
            self.line = mark

    def _append(self, content):
        self.line += content
        return self

    def line(self):
        return self.line

    def clear(self):
        self.line = ""
