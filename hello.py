# Import all the library

import requests
from bs4 import BeautifulSoup
import os

# Add urls

urls = "http://www.stickyday.com/perfectly-timed-moments-in-139-photos/"
url = [urls + str(num) for num in range(1, 140)]
ans = []

# made scrape function


def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    u = soup.findAll("img")[0]['src']
    f = open('download', 'a')
    f.write(u + "\n")
    ans.append(u)

# showing the progress of the link download


count = 1
for i in url:
    scrape(i)
    print ("DONE :" + str(count))
    count += 1

# Start downloading

print ("Starting Downloading :\n\n\n")

os.system('mkdir hello')
os.system('wget -P hello -i download')
