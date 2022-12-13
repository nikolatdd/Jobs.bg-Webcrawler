Jobs.bg Webcrawler
==================

![logo](https://user-images.githubusercontent.com/100529135/207468197-274bf10e-160d-4617-a46f-1c925c1553f0.png)

About Project
---
1. Fetch html
2. Scrape latest 20 jobs containing the required skill "Python" <br />
   => Extracting (page title, job name/title, job published date, job region, all job skills required)  
3. Store extracted data in MySql database
4. Create PyQt6 GUI to implement the steps above <br />
   => Show database data with PyQt6's TableViewWidget

Requirements
--- 
0. Have MySql installed on local machine
1. Change current working directory to main project directory -> ./Jobs.bg-Webcrawler/
2. Create virtual enviorment -> python3 -m venv .venv <br />
   Enter new virtual enviorment -> .\venv\Scripts\activate  <br />
      or  for Comand Prompt -> .\.venv\Scripts\Activate.ps1 <br /> 
      or for Powershell,Bash.. -> .\.venv\Scripts\Activate.bat
3. Install required modules -> pip install -r requirements.txt
4. Run main.py

