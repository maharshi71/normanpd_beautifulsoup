import pytest

from project0 import project0

myurl = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-16%20Daily%20Arrest%20Summary.pdf"
def test_fetchincidents():
    assert project0.fetchincidents(myurl) is not None
