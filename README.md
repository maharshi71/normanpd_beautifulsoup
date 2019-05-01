# cs5293sp19-project0
Norman, Oklahoma police department reports of incidents arrests and other activities 
== 
The website contains three types of summaries arrests, incidents, and case summaries.
The main aim of our code is to extract the data from the PDF files in the [oklahoma police department](http://normanpd.normanok.gov/content/daily-activity) and extract the data from PDF and push the data into the sqlite3 database and display a random record which is seperated by an **thorn**(þ).

---
#Author
**Sri Sai Maharshi Kondapaneni**
Author Email: maharshi@ou.edu
Packages used: urllib, PyPDF2, tempfile, sqlite3, argparse

---
#Structure 
```.
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs
├── project0
│   ├── __pycache__
│   │   └── project0.cpython-37.pyc
│   ├── main.py
│   └── project0.py
├── setup.cfg
├── setup.py
└── tests
    ├── test_db.py
    ├── test_download.py
    └── test_fields.py
 ```
#Setup Instructions
This package is used to scrape the data from the Norman Police Department's daily activity website. Give the url of the pdf, this package fetches the data from the given link, extracts the first page, stores it in a sqlite database and prints a random row of the data. The data fetched from the PDF is stored into assests table of the database called normanpd.db  Clone the github repository into you local system and run it.
**How to Run:**
--
To run this u need to pass the command line as follows:
python main.py --arrests "the link of pdf"
`python main.py --arrests "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-13%20Daily%20Arrest%20Summary.pdf"`
output:
You will get an string with thorn character which seperates the fields of the PDF
`2/12/2019 20:11þ2019-00012021þ1330 E LINDSEY STþPUBLIC INTOX / CONSUMING INTOX BEV - SPIRTSþDONALD WAYNE WRIGHTþ5/1/1965þHOMELESSþFDBDC (Jail)þ1632 - Hudson`

----
#External Resources 
https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
https://www.tutorialspoint.com/python/python_command_line_arguments.html
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/
https://www.dataquest.io/blog/regular-expressions-data-scientists/
https://docs.python.org/3.3/howto/regex.html
http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/
https://docs.python.org/2/library/tempfile.html

---

#Assumptions
This  code is hard coded for solving only the fields which have only the same format as of the pdf files in the  [oklahoma police department](http://normanpd.normanok.gov/content/daily-activity)
Assuming that the empty spaces in the pdf occur only in the city, sate, zipcode coloumns only.
And the structure of the database is of the form :
`CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
);`

---

#Bugs
1. This version only is able to handle two lines in a singel cell.
2. All cases that were found with three lines were hardcoded to match the format of the given file.
3. This program can handle only these errors `replace('Officer', 'Officer;').replace(' \n', ' ').replace('\n',',').replace( '- \n', ' ').replace('\nD - DUS','D - DUS')`

---
#Description of the Functions:
Extractincidents(): 
--
This function thaks the input from the user and opens the url and reads the data in bytes format and returns it.

---
Fetchincidents():
--
This takes the bytes input from the extract incidents and reads it into a temporary file and extracts the data using PyPDF2 and clean the data. Then we join the three columns in the list (city,state,zipcode) to the arestee address. And then send the list of lists as the output.

---
Createdb():
--
The createdb() function creates an SQLite database file named normanpd.db and inserts a table with the schema below.
```
CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
);
```
---
Populatedb():
--
The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database.

---
Status():
--
The status() function prints to standard out, a random row from the database. Each field of the row should be separated by the thorn character (þ).

