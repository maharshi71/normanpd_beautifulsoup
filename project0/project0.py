import argparse
import tempfile
import urllib.request
from bs4 import BeautifulSoup
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas
import sqlite3

def fetchincidents():
    url = ("http://normanpd.normanok.gov/content/daily-activity")
    
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data,'html.parser')
    tags = soup.find_all('a', href = re.compile("Arrest"))
    link= []
    for t in tags:
        link.append(t.get('href'))
    links = []
    for i in range(len(link)):
        links.append("http://normanpd.normanok.gov"+link[i])
    (links)
    return(links)

def extractincidents():
    url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-13%20Daily%20Arrest%20Summary.pdf"
    data = urllib.request.urlopen(url)
    
    fp = tempfile.TemporaryFile()
    
    # Write the pdf data to a temp file
    fp.write(data.read())
    
    # Set the curser of the file back to the begining
    fp.seek(0)
    
    
    
    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()
    
    # Get the first page
    page1 = pdfReader.getPage(0).extractText().replace('Officer','Officer;').replace(' \n',' ').replace('\n',',').replace('- \n',' ').split(";")
    for i in range(len(page1)):
        page1[i]=page1[i].strip(',')
    #print((page1[1]))
    final=[]
    for i in range(0,len(page1)-1):
        lp=page1[i].split(',')
        #print(lp)
        if (len(lp)== 12):
            lp[6] = ','.join(lp[6:10])
            #print(lp)
            lp.pop(7)
            lp.pop(-3)
            lp.pop(-3)
            final.append(lp)
        elif (len(lp)==11):
            lp[6]= ','.join(lp[6:9])
            #print(lp)
            lp.pop(7)
            lp.pop(-3)
            final.append(lp)
        elif (len(lp)==10):
            lp[6]=','.join(lp[6:8])
            #print(lp)
            lp.pop(7)
            final.append(lp)
        else:
            final.append(lp)
    #print(final)
for it in final:
    print(len(it),it)
    df=pandas.DataFrame(final)
    df = df[1:]
    header=['Arrest Date / Time','Case Number','Arrest Location','Offense','Arrestee','Arrestee Birthday','Arrestee Address,City,State,Zip Code','Status','Officer']
    df.columns = header
    print(df)
    return df
    
    '''
        gr=[]
        for item in page1:
        #match=re.findall(r'\d{1}/\d{1}/\d{4}.*\,[F]',item)
        match= re.findall(r'HOMELESS.*',item)
        #match[0]=match[0][0:len(match[0])-2]
        gr.append(match)
        
        print(gr)
        for item in gr:
        if len(item)!=0:
        item[0]=item[0][0:len(item[0])-2]
        print(gr)
        #print(len(gr[1]))
        #for i in range(len(gr)):
        #    if(len(gr[i])==0):
        #        gr.pop(i)
        #print(gr)
        return '' '''
def createdb():
    sql = sqlite3.connect('normanpd.db')
    cur = sql.cursor()
    
    abc = """CREATE TABLE IF NOT EXISTS arrests (arrest_time TEXT,case_number TEXT,arrest_location TEXT,offense TEXT,arrestee_name TEXT,arrestee_birthday TEXT,arrestee_address TEXT,status TEXT,officer TEXT)"""
    cur.execute(abc)
    
    return ''

def populatedb(incidents):
    sql = sqlite3.connect('normanpd.db')
    cur = sql.cursor()
    for x,i in incidents.iterrows():
        cur.execute("INSERT INTO arrests(?,?,?,?,?,?,?,?,?)",(i['Arrest Date/Time'],i['Case Number'],i['Arrest Location'],i['Offence'],i["Arrestee"],i['Arrestee Birthday'],i['Arrestee Address,City,State,Zip Code'],i['Status'],i['Officer']))
    cur.execute("SELECT * FROM arrests ORDER BY Random() LIMIT 1")
    res= cur.fetchall()
    for e in res:
        print(e)

#def status(db)


#SELECT * FROM table WHERE id IN (SELECT * FROM table ORDER BY RANDOM() LIMIT x)
#SELECT * FROM arrests ORDER BY Random() LIMIT 1
#print (fetchincidents())'''
incidents = extractincidents()
createdb()
populatedb(incidents)
