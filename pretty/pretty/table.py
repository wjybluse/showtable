__author__ = 'wan'
import formatter
from pretty.tools.utils import *
from pretty.tools.builder import *


class PrettyTable(formatter.Formatter):
    def __init__(self, message, func=None, filtes=dict()):
        formatter.Formatter.__init__(message, func, filtes)

    def show(self):
        for line in self.message:
            print(line)

    def create(self):
        self.message = eval(self.message)
        self._before_filter()
        self.message = handle_json(self.message)

    def _before_filter(self):
        if self.filters is not None:
            (self.message.pop(key) for key in self.filters)


def handle_json(message=dict()):
    return handle_normal_json(message)


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
        return handle_complex_list(message)

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
    # list component has some situation
    # 1.list contains same json object
    # 2.list contains diff json object
    item = message[0]
    if isinstance(item, dict):
        keys = item.keys()
        val = [val for val in message if isinstance(val, dict) and val.has_key(key) for key in keys]
        if len(val) == len(message):
            return handle_simple_list({"message": message})
    else:
        return _check_other(message)


def _check_other(message):
    """
    :rtype : object
    """
    flag = True
    for val in message:
        if isinstance(val, dict):
            flag = False
    if not flag:
        return _handle_normal_list(message)
    table = dict(Index="Value")
    for index in range(0, len(message)):
        table[index] = message[index]
    return _create_table(table)


def handle_complex_list(message=dict()):
    pass


def _handle_normal_list(message):
    pass


def _create_table():
    pass









