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
    return table


def handle_simple_list(message=dict()):
    keys, values = list(message.keys()), list(message.values())
    count_list = 0
    list_component = None
    for value in values:
        if isinstance(value, list):
            count_list += 1
            list_component = value
    if count_list > 1:
        return handle_compex_list(message)

    if list_component is None:
        return handle_normal_json(message)

    comp_elm = max(list_component, key=lambda el: len(el) if isinstance(el, dict) else 0)
    table = _create_simple_table(comp_elm.keys(), list_component)
    return _handle_table(table)


def _create_simple_table(keys, component):
    table = dict()
    for key in keys:
        table[key] = []
        table[key].append(key)

    for el in component:
        if not isinstance(el, dict):
            continue
        for key, val in el.items():
            table[key].append(val)
    for title, value in table.items():
        table[title].append(get_max_length(value))
    return table


def _handle_table(table):
    result = []
    values = list(table.values())
    for i in range(0, len(values[0])):
        sb = StringBuilder()
        title = StringBuilder()
        sb = sb.append(BEGIN)
        title = title.append("|")
        for j in range(0, len(values)):
            mx = values[j][-1]
            sb = sb.append(create_border(mx))
            title = title.append(create_cell(mx, values[j][i]))
        result.append(sb.line)
        result.append(title.line)
    result.append(result[0])
    return result


def handle_list(message=list()):
    pass


def handle_compex_list(message=dict()):
    pass









