"""
author: wensong
time :2017.12.21
function:make a easy spider to download some picture
"""

import mechanize
import time
from bs4 import BeautifulSoup
import string
import urllib

start = "http://" +raw_input("Where would you like to start searching?\n")
br = mechanize.Browser()
r = br.open(start)
html = r.read()
soup = BeautifulSoup(html)
for link in soup.find_all('a'):
    print (link.get('href'))
