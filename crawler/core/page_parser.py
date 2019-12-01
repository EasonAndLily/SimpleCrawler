import re
import urlparse

from bs4 import BeautifulSoup


class PageParser(object):
    @classmethod
    def parser(cls, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        urls = cls.__get_new_urls(url, soup)
        data = cls.__get_new_data(url, soup)
        return urls, data

    @classmethod
    def __get_new_urls(cls, url, soup):
        urls = set()
        links = soup.findAll('a', href=re.compile(r'/item/([\s\S]*)/\d+'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            urls.add(new_full_url)

        return urls

    @classmethod
    def __get_new_data(cls, url, soup):
        res_data = {}
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.getText()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.getText()
        res_data['url'] = url
        return res_data
