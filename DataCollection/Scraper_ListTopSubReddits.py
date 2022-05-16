#getting a list of top reddits
#initial try is to use https://redditlist.com as source

import requests
from bs4 import BeautifulSoup
result = requests.get('http://redditlist.com/')
src = result.content
soup = BeautifulSoup(src, 'html.parser')

#first try, commented out, because below is lsightly better
#subs_links = []
#for a in soup.find_all('a', class_="sfw"):
#    subs_links.append(a['href'])
#subs_links[:]
# #   xpath: /html/body/div[4]/div[3]/div[1]/div[2]

#slightly better, but still takes all listed URLs of all three categories..
subs_links_2 = []
data_test = soup.find_all('div', attrs={'class':"listing-item"})
for div in data_test:
    linkers = div.find_all('a')
    for a in linkers:
        subs_links_2.append(a['href'])
subs_links_2[:]