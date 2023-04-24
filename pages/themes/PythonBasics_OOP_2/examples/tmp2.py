# import urllib2
from bs4 import BeautifulSoup as bs

quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)

soup = bs(page,'html.parser')