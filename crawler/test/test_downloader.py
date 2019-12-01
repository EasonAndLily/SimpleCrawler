import unittest
from unittest import TestCase

from crawler.core.downloader import Downloader


class TestDownloader(TestCase):

    def test_downloader_page(self):
        url = "https://baike.baidu.com/item/Python/407313"
        content = Downloader.downloader_page(url)
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()
