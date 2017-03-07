#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
html = urlopen('https://litemind.com/best-famous-quotes/').read()
soup=BeautifulSoup(html, 'html.parser')
ans=[]
for section in soup.findAll('div',{"class":"wp_quotepage"}):
	quotes = section.findChildren()[0].text
	author = section.findChildren()[1].text
	print (quotes, author)
	f=open('Helloki','a')
	f.write(quotes + author +"\n")
	ans.append(quotes)
	f.close()

