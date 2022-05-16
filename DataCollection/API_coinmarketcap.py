  #API_coinmarketcap

#  Using the coinmarketcap API to fetch latest prices.
#  //Lot of other features also available:
#  - data: [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 9647, 'date_added': '2013-04-28T00:00:00.000Z',
#  - tags: ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio']
#

import numpy as np
import pandas as np
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',  #amount of cryptocurrencies (1 = btc, 2= eth etc..)
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '001e66e2-5fda-4956-bdde-c0c9129c02c5',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
  price=data['data'][0]['quote']['USD']['price']
  print(round(price, 2))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  

  #print('------------')