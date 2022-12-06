import requests
# import os
from bs4 import BeautifulSoup
import re
from datetime import datetime as datetime

# Local imports
try:
	from constants import DATA_PATH,BASE_URL
	from decorator import count_timer
	from db import DB
except:
	from lib.constants import DATA_PATH,BASE_URL
	from lib.decorator import count_timer
	from lib.db import DB



class Crawler():
	def __init__(self, base_url:str()):
		self.seed = [base_url]
		self.db = DB()

	def write_to_file(self,filename:str(), content:str()):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""
		with open(DATA_PATH+filename, "w", encoding="utf-8") as f:
			f.write(content)

	def get_html(self, url:str()):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification
			:param url: string
		"""
		r = requests.get(url)
		if r.ok:
			# r.encoding = "windows-1251"
			return r.text
	
	def scrape_html(self, filename:str()):
		""" Scrape - (title:string,date:string,location:string,skills:list) """
		job_titles = list()
		job_dates = list()
		job_locations = list()
		job_skills = list()


		with open(DATA_PATH+filename, "r", encoding="utf8") as fp:
			soup = BeautifulSoup(fp, "html.parser")
			homepage_title = soup.title.text
			print(homepage_title)
			cards_list = soup.find(class_="cards-list") 
			job_cards = soup.find_all("li",class_ = range(21))

			for job in job_cards:
				#titles
				title = job.find("a", class_ = "black-link-b")
				job_titles.append(title["title"])

				# Date
				date = job.find("div", class_="card-date")
				date = date.next_element.text
				date = re.sub("[\s]","", date)
				if date.lower() in ["днес", "вчера"]:
					date = datetime.today()
					date = date.strftime("%d.%m.%y")
				date = datetime.strptime(date,"%d.%m.%y").date()
				job_dates.append(str(date))
				
				# Location
				location = job.find("div", class_="card-info card__subtitle")
				location = location.next_element.text
				location = re.sub("[\s;]","", location)
				job_locations.append(location)
				
				#Skills
				#todo: bad written
				skillset = job.find("div", attrs={"style": "float: left"})
				if skillset is None:
					job_skills.append([str()])
				else:
					skill_each = list()
					skillset = skillset.find_all("img")
					[skill_each.append(skill["alt"]) for skill in skillset]
						
					job_skills.append(skill_each)

			# try:
			# 	for title_, date_, loc_, skills_ in zip(job_titles,job_dates,job_locations, job_skills, strict=True):
			# 		print(title_, date_, loc_, skills_, sep="\n")
			# 		break
			# except:
			# 	print(f"""!!!Job/s missing either:
			# 	titles:{len(job_titles)}
			# 	dates {len(job_dates)}
			# 	locations {len(job_locations)}
			# 	skills: {len(job_skills)}""")
		
		return [[title, date, loc, str(",".join(skills))] for title, date, loc, skills in zip(job_titles,job_dates,job_locations,job_skills)]

	@count_timer
	def run(self):
		""" run the crawler for each url in seed
			Use multithreading for each GET request
		"""
		for url in self.seed:
			html = self.get_html(url)
			self.write_to_file("jobs.bg.html", html)

		content = self.scrape_html("jobs.bg.html")	
		self.db.drop_jobsbg_table()
		self.db.create_jobsbg_table()
		self.db.insert_rows(content)

		print("Crawler finished its job!")


if __name__ == "__main__":
	crawler = Crawler(BASE_URL)
	crawler.run()