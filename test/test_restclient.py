__author__ = 'wan'
import unittest

from restserver.restclient import RestClient


class TestRestClient(unittest.TestCase):
    def test_get_method(self):
        client = RestClient("http", "127.0.0.1", 3000, "/blog/show/1")
        value = client.get()
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_post_method(self):
        client = RestClient("http", "127.0.0.1", 3000, "/blog/show/1")
        value = client.post('{"nihao":"hahha"}')
        print(value)
        self.assertNotRegex(value, "errorReason")

    def test_put_method(self):
        client = RestClient("https", "127.0.0.1", 5000, "/blog/show/1")
        value = client.put('{"nihao":"hahha"}')
        print(value)
        self.assertNotRegex(value, "errorReason")


if __name__ == "__main__":
    unittest.main()
