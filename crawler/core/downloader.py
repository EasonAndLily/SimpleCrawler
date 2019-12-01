import ssl
import urllib2


class Downloader(object):

    @classmethod
    def downloader_page(cls, url):
        if url is None:
            return None
        req = urllib2.Request(url)
        content = ssl._create_unverified_context()
        response = urllib2.urlopen(req, context=content)
        if response.code != 200:
            return None
        return response.read()
