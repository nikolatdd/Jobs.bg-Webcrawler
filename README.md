#Jobs.bg Webcrawler

#H1 About Project
---
1. Fetch html
2. Scrape latest 20 jobs containing the required skill "Python"
   => Extracting (page title, job name/title, job published date, job region, all job skills required)
3. Store extracted data in MySql database
4. Create PyQt6 GUI to implement the steps above
   => Show database data with PyQt6's TableViewWidget

#H1 Requirements
--- 
0. Have MySql installed on local machine
1. Change current working directory to main project directory -> ./Jobs.bg-Webcrawler/
2. Create virtual enviorment -> python3 -m venv .venv
   Enter new virtual enviorment -> .\venv\Scripts\activate
      or  for Comand Prompt -> .\.venv\Scripts\Activate.ps1
      for Powershell,Bash.. -> .\.venv\Scripts\Activate.bat
3. Install required modules -> pip install -r requirements.txt
4. Run main.py
	
