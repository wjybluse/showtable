__author__ = 'wan'
import formatter
from pretty.tools.utils import *
from pretty.tools.builder import *


class PrettyTable(formatter.Formatter):
    def __init__(self, message, func=None, filtes=dict()):
        formatter.Formatter.__init__(message, func, filtes)

    def show(self):
        pass

    def create(self):
        self.message = eval(self.message)
        # create table if message is simply json
        pass


def handle_normal_json(message=dict()):
    table = []
    prop, value = titles()
    keys, values = list(message.keys()), list(message.values())
    keys.append(prop)
    values.append(value)
    max_key = get_max_length(keys)
    max_value = get_max_length(values)
    sb = StringBuilder()
    sb.append(BEGIN) \
        .append(create_border(max_key)) \
        .append(create_border(max_value))
    table.append(sb.line)
    for index in range(0, len(keys) - 1):
        line = StringBuilder()
        line.append("|") \
            .append(create_cell(max_key, keys[index])) \
            .append(create_cell(max_value, values[index]))
        table.append(line.line)
        table.append(sb.line)


def handle_simple_list(message=dict()):
    pass


def handle_compex_list(message=dict()):
    pass









