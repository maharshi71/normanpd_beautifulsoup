import pytest
import sqlite3
from project0 import project0

url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-13%20Daily%20Arrest%20Summary.pdf"
database='normanpd.db'
def test_createdb():
    dbname = project0.createdb()
    assert dbname == database
    assert dbname == database
def test_populatedb():
    sql = sqlite3.connect(database)
    cur = sql.cursor()
    cur.execute('select * from arrests order by random() limit 1')
    result = cur.fetchall()
    assert result is not None
def test_fetchincidents():
    assert project0.fetchincidents(url) is not None
