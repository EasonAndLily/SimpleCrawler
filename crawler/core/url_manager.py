class UrlManager(object):
    def __init__(self):
        self.__urls = set()
        self.__accessed_urls = set()

    def get_urls(self):
        return self.__urls

    def add_url(self, url):
        if url is None or url in self.__urls:
            return
        self.__urls.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    def has_url(self):
        return len(self.get_urls()) > 0

    def get_url(self):
        url = self.__urls.pop()
        self.__accessed_urls.add(url)
        return url
