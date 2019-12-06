import os
import unittest
from unittest import TestCase

from crawler.core.outputer import Outputer


class TestOutputer(TestCase):
    def test_outputer_html(self):
        summary = u'\nPython\u662f\u4e00\u79cd\u8de8\u5e73\u53f0\u7684\u8ba1\u7b97\u673a\u7a0b\u5e8f\u8bbe\u8ba1' \
                  u'\u8bed\u8a00\u3002\u662f\u4e00\u79cd\u9762\u5411\u5bf9\u8c61\u7684\u52a8\u6001\u7c7b\u578b\u8bed' \
                  u'\u8a00\uff0c\u6700\u521d\u88ab\u8bbe\u8ba1\u7528\u4e8e\u7f16\u5199\u81ea\u52a8\u5316\u811a\u672c(' \
                  u'shell)\uff0c\u968f\u7740\u7248\u672c\u7684\u4e0d\u65ad\u66f4\u65b0\u548c\u8bed\u8a00\u65b0\u529f' \
                  u'\u80fd\u7684\u6dfb\u52a0\uff0c\u8d8a\u6765\u8d8a\u591a\u88ab\u7528\u4e8e\u72ec\u7acb\u7684\u3001' \
                  u'\u5927\u578b\u9879\u76ee\u7684\u5f00\u53d1\u3002\n                \n'
        data = {
            'summary': summary,
            'title': 'Python',
            'url': 'https://baike.baidu.com/item/Python/407313'
        }
        outputer = Outputer()
        outputer.collect_data(data)
        file_path = os.path.dirname(os.path.abspath(__file__))
        file_name = 'test.html'
        outputer.outputer_html(file_path, file_name)

        self.assertTrue(os.path.isfile(os.path.join(file_path, file_name)))


if __name__ == '__main__':
    unittest.main()
