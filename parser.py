import urllib2
from bs4 import BeautifulSoup 

html = urllib2.urlopen("http://example.webscraping.com/")

soup = BeautifulSoup(html)