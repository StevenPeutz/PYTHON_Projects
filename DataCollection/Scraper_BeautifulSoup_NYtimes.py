# Creating a csv file from nytimes article on all Trump lies 
# "Text to data"
# Thanks to Kevin Markham 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#actual url and bs4 necessities:
url = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#the magic line:
results = soup.find_all('span', attrs={'class':'short-desc'})
#testing:
#print(len(results))
#first_result = results[0]
#print(first_result.contents[1])

#creating data set:
records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    check = result.find('a').text[1:-1]
    link = result.find('a')['href']
    records.append((date, lie, factcheck, link))
print(len(records))
print(records[0:1])

import pandas as pd  
df = pd.DataFrame(records, columns=['date', 'lie', 'factcheck', 'link']) 

#make date format more universal (for analysis):
df['date'] = pd.to_datetime(df['date'])  

#turn to csv:
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')  

#reading it back to pandas from csv:
#df = pd.read_csv('trump_lies.csv', parse_dates=['date'], encoding='utf-8')
