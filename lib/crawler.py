import requests
import os
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Local imports
try:
	from constants import DATA_PATH, BASE_URL
	from decorators import count_timer
except:
	from lib.constants import DATA_PATH, BASE_URL
	from lib.decorators import count_timer



class Crawler():
	def __init__(self, base_url):
		self.seed = [base_url]

	def write_to_file(self,filename, content):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""
		with open(DATA_PATH+filename, "w", encoding="utf-8") as f:
			f.write(content)

	def get_html(self, url):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification
			:param url: string
		"""
		r = requests.get(url)
		if r.ok:
			# r.encoding = "windows-1251"
			return r.text
	
	def scrape_html(self, filename):
		job_titles = list()
		job_dates = list()
		job_locations = list()
		job_skills = list()
		

		with open(DATA_PATH+filename, "r", encoding="utf8") as fp:
			soup = BeautifulSoup(fp, "html.parser")
			cards_list = soup.find(class_="cards-list") # обяви

			#titles
			titles = cards_list.find_all("a", class_ = "black-link-b")
			[job_titles.append(title["title"]) for title in titles]

			# Date
			for date in cards_list.find_all("div", class_="card-date"):
				date = date.next_element.text
				date = re.sub("[\s]","", date)
				if date.lower() in ['днес', 'today']:
					date = datetime.now()
					date = date.strftime("%d.%m.%y")
				job_dates.append(date)
			
			# Location
			for location in cards_list.find_all("div", class_="card-info card__subtitle"):
				location = location.next_element.text
				location = re.sub("[\s;]","", location)
				job_locations.append(location)

			# Interview todo
			# for interview in cards_list.find_all("span", attrs={"style": "white-space: nowrap;"}):
			# 	interview = interview.text
			
			#Skills
			skills = cards_list.find_all("div", attrs={"style": "float: left"})
			for skillset in skills:
				skillset_each_job = list() 			
				subskillset = skillset.find_all("img")
				for skill in subskillset:
					skill = skill['alt']
					skillset_each_job.append(skill)
				job_skills.append(skillset_each_job)

				
			try:
				for title_, date_, loc_, skills_ in zip(job_titles,job_dates,job_locations, job_skills, strict=True):
					print(title_, date_, loc_, skills_, sep="\n")
					break
			except:
				print(f"""!!!Job/s missing either:
				titles:{len(job_titles)}
				dates {len(job_dates)}
				locations {len(job_locations)}
				skills: {len(job_skills)}""")

	@count_timer
	def run(self):
		""" run the crawler for each url in seed
			Use multithreading for each GET request
		"""
		for url in self.seed:
			html = self.get_html(url)
			self.write_to_file("jobs.bg.html", html)
		self.scrape_html("jobs.bg.html")

		print("Crawler finished its job!")


if __name__ == "__main__":
	crawler = Crawler(BASE_URL)
	crawler.run()