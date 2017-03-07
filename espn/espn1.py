from bs4 import BeautifulSoup
import urllib.request

f=open('Esp.txt','w')
errorf= open ('esperror.txt','w')

c=0
x=0
while (x < 500):
	soup = BeautifulSoup(urllib.request.urlopen('http://games.espn.com/ffl/tools/projections?startIndex='+str(x)).read(),'html.parser')		
	table = soup.find("table",{"class" : "playerTableTable tableBody"})
	for row in table.findAll('tr')[2:]:
		col = row.findAll('td')

		try:
			name=col[0].a.string.strip()
			f.write(name+'\n')
			c+=1
			print (c)
		except Exception as e:
			errorf.write (str(x) + '*******' + str(e)+ '******' + str(col) + '\n')
			pass
	x = x + 40

f.close
errorf.close
	

