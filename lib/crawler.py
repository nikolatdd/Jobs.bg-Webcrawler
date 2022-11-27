import requests
import os
from bs4 import BeautifulSoup

# Local imports
if __name__ == '__main__':
	from constants import DATA_PATH
	from constants import BASE_URL
	from decorators import count_timer
else:
	from lib.constants import DATA_PATH
	from lib.constants import BASE_URL
	from lib.decorators import count_timer



class Crawler():
	def __init__(self, base_url):
		self.seed = [base_url]

	def write_to_file(self,filename, content):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""
		with open(DATA_PATH+filename, 'w', encoding='utf-8') as f:
			f.write(content)

	def get_html(self, url):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification
			:param url: string
		"""
		r = requests.get(url)
		if r.ok:
			r.encoding = 'windows-1251'
			return r.text

	@count_timer
	def run(self):
		""" run the crawler for each url in seed
			Use multithreading for each GET request
		"""
		for url in self.seed:
			html = self.get_html(url)
			self.write_to_file('jobs.bg.html', html)


		print('Crawler finished its job!')


if __name__ == '__main__':
	crawler = Crawler(BASE_URL)
	crawler.run()