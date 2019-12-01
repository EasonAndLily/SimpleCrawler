import unittest

from crawler.core.url_manager import UrlManager


class TestUrlManager(unittest.TestCase):
    def setUp(self):
        self.url_manager = UrlManager()

    def test_add_url(self):
        self.url_manager.add_url("http://www.google.com")
        self.assertTrue("http://www.google.com" in self.url_manager.get_urls())

    def test_add_urls(self):
        urls = ["http://www.google.com", "http://www.baidu.com", "http://baike.baidu.com"]
        self.url_manager.add_urls(urls)
        self.assertTrue(all(elem in urls for elem in self.url_manager.get_urls()))

    def test_has_url(self):
        self.url_manager.add_url("http://www.google.com")
        self.assertTrue(self.url_manager.has_url())

    def test_get_url(self):
        self.url_manager.add_url("http://www.baidu.com")
        self.assertEqual(len(self.url_manager.get_urls()), 1)

        url = self.url_manager.get_url()
        self.assertEqual(url, "http://www.baidu.com")
        self.assertEqual(len(self.url_manager.get_urls()), 0)


if __name__ == '__main__':
    unittest.main()
