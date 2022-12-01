import os

from lib.crawler import Crawler
from lib.constants import BASE_URL


if __name__ == '__main__':
	crawler = Crawler(BASE_URL)
	crawler.run()