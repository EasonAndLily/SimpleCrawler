from outputer import Outputer
from page_parser import PageParser
from url_manager import UrlManager
from downloader import Downloader


class Crawler(object):
    def __init__(self, url, path, file_name):
        self.url_manager = UrlManager()
        self.url_manager.add_url(url)
        self.path = path
        self.file_name = file_name
        self.outputer = Outputer()

    def crawler(self):
        count = 0
        while self.url_manager.has_url():
            # noinspection PyBroadException
            try:
                url = self.url_manager.get_url()
                print "craw %d:%s" % (count, url)
                content = Downloader.downloader_page(url)
                urls, data = PageParser.parser(url, content)
                self.url_manager.add_urls(urls)
                self.outputer.collect_data(data)

                if count == 10:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.outputer_html(self.path, self.file_name)
