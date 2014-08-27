__author__ = 'wan'
import unittest

from pretty.pretty.table import *


class TableTest(unittest.TestCase):
    def test_create_table(self):
        dd = {"dsa": [{"name": "hahha", "age": 123, "sex": "male"}, {"name": "dada", "age": 543, "sex": "dadasdas"},
                      {"name": "dasdsa", "age": 4324, "sex": "dassda"}]}
        rest = handle_simple_list(dd)
        for item in rest:
            print(item)