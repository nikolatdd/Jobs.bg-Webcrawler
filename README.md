<h1 align="center"> Jobs.bg Webcrawler </h1>

![logo](https://user-images.githubusercontent.com/100529135/207468197-274bf10e-160d-4617-a46f-1c925c1553f0.png) <br />
**Author**: nikolatdd <br />
**Created**: November-December 2022 <br />

About Project
---
1. Scrape latest 20 jobs containing the required skill "Python" <br />
   and extract: page title, job title, job published date, job region, all job skills required  
2. Store extracted data in MySql database
3. Implement data on PyQt6 GUI table

Requirements
--- 
0. Configure MySql data in config.ini
1. Create virtual enviorment: python -m venv .venv <br />
   Enter new virtual enviorment: .\venv\Scripts\activate  <br />
      or for Comand Prompt: .\.venv\Scripts\Activate.ps1 <br /> 
      or for Powershell,Bash: .\.venv\Scripts\Activate.bat
2. Install required python modules: pip install -r requirements.txt
3. Run app.py

