__author__ = 'wan'
import unittest

from pretty.rest.rest import RestClient


class TestRestClient(unittest.TestCase):
    def test_get_method(self):
        client = RestClient("http", "127.0.0.1", 3000)
        value = client.get(url="/blog/show/1")
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_post_method(self):
        client = RestClient("http", "127.0.0.1", 3000)
        value = client.post('{"nihao":"hahha"}', url="/blog/show/1")
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_put_method(self):
        client = RestClient("https", "127.0.0.1", 5000)
        value = client.put('{"nihao":"hahha"}', url="/blog/show/1")
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_add_headers(self):
        client = RestClient("http", "127.0.0.1", 3000)
        value = client.add_headers({"hahhah": "hhehehe"}).get(url='/blog/show/1')
        print(value)
        self.assertNotRegex(value, "errorReason")


if __name__ == "__main__":
    unittest.main()
