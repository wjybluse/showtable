__author__ = 'wan'
BEGIN = END = "+"


class StringBuilder():
    def __init__(self):
        self.line = ""

    def append(self, content):
        assert isinstance(content, object)
        self.line = "{0}{1}".format(self.line, content)
        return self

    @property
    def line(self):
        return self.line

    @property
    def end_border(self):
        self.line = "{0}{1}".format(self.line, END)
        return self

    @property
    def end_cell(self):
        self.line = "{0}{1}".format(self.line, "|")
        return self

    @property
    def clear(self):
        self.line = ""
        return self


def create_cell(max_len, content=None):
    content_size = len(str(content))
    if max_len == content_size:
        return "{0}|".format(content)
    if max_len < content_size:
        raise ValueError("The content is invalid,content {0}".format(content))
    return "{0}{1}".format(content, _create_space(max_len - content_size))


def create_border(width):
    if width <= 0:
        raise TypeError("The border type is error.The len is 0")
    return _row(width)


def _create_space(count):
    return _space(count)


def _space(count):
    if count == 0:
        return "|"
    s = ""
    for i in range(0, count):
        s = "{0} ".format(s)
    return "{0}|".format(s)


def _row(width):
    s = ""
    for i in range(0, width):
        s = "{0}-".format(s)
    return "{0}{1}".format(s, END)
