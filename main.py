import json
import os

from crawler.core.crawler import Crawler

if __name__ == "__main__":
    with open('./config/config.json') as config_file:
        config = json.load(config_file)
        path = config["path"]
        if path is None:
            path = os.path.dirname(os.path.abspath(__file__)) + "/output"
        crawler = Crawler(config["url"], path, config["file_name"])
        crawler.crawler()
