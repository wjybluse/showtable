__author__ = 'wan'

MARK = '|'

from pretty.table.builder import BuildLine


class ShowJsonTable():
    """the class is suitable for showing the json table like this:
    1.the normal json object,example:
        {"key1":"value","key2":"value2"}
    2.the list style of json array,example:
        {"app":[{"name":"value","style":"normal","color":"read","number":"hhehhe"}]}
    """

    def __init__(self, json=None):
        self.json = json

    def create_table(self):
        result = eval(str(self.json))

        for k, v in result.items():
            if isinstance(v, list):
                self.handle_list_component(result)
                return

        self.handle_normal_json(result)


    # parse the normal json
    def handle_normal_json(self, json=dict()):
        """
        :param json:
        """
        keys, values = json.keys(), json.values()
        max_key, max_value = get_max_length(arr=list(keys)), get_max_length(arr=list(values))
        self.show_table(keys, values, max_key=max_key, max_value=max_value)

    # parse the json array
    def handle_list_component(self, json=dict):
        cache = {}
        for k, v in json.items():
            for item in v:
                for pk, pv in item.items():
                    if not cache.__contains__(pk):
                        cache[pk] = []
                    cache[pk].append(pv)

        result_keys, result_values = cache.keys(), cache.values()

        write = self.write_one_row(result_keys, result_values)

        title = BuildLine(MARK)
        for k, v in zip(result_keys, result_values):
            title._append(k + get_space(list(v)[-1], len(k)) + MARK)
        write(title.line)

        h2l_values = list(result_values)
        first_values = h2l_values[0]
        for index in range(0, len(first_values) - 1):
            v_line = BuildLine(MARK)
            f_item = str(first_values[index])
            v_line._append(f_item + get_space(first_values[-1], get_len(f_item)) + MARK)
            for item_index in range(1, len(h2l_values)):
                list_item = h2l_values
                r_item = str(list_item[item_index][index])
                v_line._append(r_item + get_space(list_item[item_index][-1], get_len(r_item)) + MARK)
            write(v_line.line)
        write(None)

    def write_one_row(self, keys, values):
        line = BuildLine("+")
        for k, v in zip(keys, values):
            max_line = max(len(k), get_max_length(v))
            v.append(max_line)
            line._append(get_line(max_line))

        def _write_one_row(content):
            print(line.line)
            if content is not None or len(str(content)) <= 0:
                print(content)

        return _write_one_row


    def show_table(self, keys, values, max_key=0, max_value=0):
        key, value = get_header()
        if len(key) > max_key:
            max_key = len(key)
        if len(value) > max_value:
            max_value = len(value)
        head = line = end = "+%s%s" % (get_line(max_key), get_line(max_value))
        print(head)
        print(self.get_string_line(key, value)(max_key, max_value))
        for k, v in zip(keys, values):
            print(line)
            print(self.get_string_line(k, v)(max_key, max_value))
        print(end)


    def get_string_line(self, p_key, p_value):
        def create_space(max_key=0, max_value=0):
            key, value = get_space(max_key, len(p_key)), get_space(max_value, len(p_value))
            return "|%s%s|%s%s|" % (p_key, key, p_value, value)

        return create_space


def get_max_length(arr=list()):
    """
    :max_length : int the max length of value
    """
    if len(arr) <= 0:
        return 0
    try:
        return len(max(arr, key=lambda item: len(str(item))))
    except Exception:
        return 0


def get_len(arg):
    try:
        return len(str(arg))
    except Exception:
        return 0


def get_header():
    return ["Property", "Value"]


def get_line(s_len):
    s = BuildLine("")
    for i in range(0, s_len):
        s._append("-")
    return s._append("+").line


def get_space(max_len, actual_len):
    s = BuildLine("")
    for i in range(actual_len, max_len):
        s._append(" ")
    return s.line


if __name__ == "__main__":
    # test_json = {"dadasdsadsa": "davfssadasdasdsadadas", "dasdsadsada": "dasxczxcsadasdss",
    # "fscsarersdas": "caadasdsadsad", "dasfsddewwsds": "dasdsadsadsa"}
    test_json = {"app": [
        {"name": "wang", "age": 24, "height": "166cm", "birthday": "1990-2-23", "city": "shenzhen", "conutry": "China"},
        {"name": "xu", "age": 25, "height": "175cm", "birthday": "1989-5-23", "city": "changsha", "conutry": "China"},
        {"name": "xie", "age": 22, "height": "180cm", "birthday": "1992-3-21", "city": "fujian", "conutry": "China"}]}
    p = ShowJsonTable(test_json)
    p.create_table()

