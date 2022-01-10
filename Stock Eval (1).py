#!/usr/bin/env python
# coding: utf-8

# In[10]:


import financedatabase as fd
import json
import pandas as pd
import re
from bs4 import BeautifulSoup
import urllib.request
import requests
from lxml import html as HTMLParser


# In[11]:


#Sectors
sectors = {
    'Technology',
    'Services',
    'Basic Materials',
    'Industrials',
    'Healthcare',
    'Financial Services',
    'Consumer Defensive',
    'Consumer Cyclical',
    'Communication Services'
}


# In[12]:


for x in sectors:
    data = fd.select_equities(country='United States', sector = x)
    ticker = list(data.keys())

    # Specifying Ticker 
    for x in range(1): # 1 ticker per industry
        tick = ticker[x]

        # Getting Info
        name = data[ticker[x]]['short_name']
        sector = data[ticker[x]]['sector']
        cap = data[ticker[x]]['market_cap']
        industry = data[ticker[x]]['industry']

        # Printing
        print(tick)
        print(name)
        print(sector)
        print(cap)
        print(" ")


# In[2]:


# Enter a stock symbol
index= 'MSFT'
# URL link 
url_is = 'https://finance.yahoo.com/quote/' + index + '/financials?p=' + index
url_bs = 'https://finance.yahoo.com/quote/' + index +'/balance-sheet?p=' + index
url_cf = 'https://finance.yahoo.com/quote/' + index + '/cash-flow?p='+ index


# In[3]:


req = urllib.request.Request(url_is)
# Customize the default User-Agent header value:
req.add_header('User-Agent', 'Mozilla/5.0')
read_data = urllib.request.urlopen(req).read()
soup_is = BeautifulSoup(read_data,'lxml')


# In[4]:


ls= [] # Create empty list
for l in soup_is.find_all('div'): 
  #Find all data structure that is ‘div’
  ls.append(l.string) # add each element one by one to the list
 
ls = [e for e in ls if e not in ('Operating Expenses','Non-recurring Events')]
new_ls = list(filter(None,ls))
new_ls = new_ls[12:]
new_ls[0] = 'Years'
new_ls[1] = new_ls[2]
new_ls[2] = new_ls[3]
new_ls[3] = new_ls[4]
new_ls[4] = new_ls[5]
new_ls[5] = new_ls[6]
new_ls[6] = 'Total Revenue'
new_ls.insert(24,"Operating Expense")
new_ls.insert(36,"Net Non Op Int")
new_ls.insert(42,"Other Income Expense")
new_ls.insert(60,"Net Income Common")
is_data = list(zip(*[iter(new_ls)]*6))


# In[13]:


years = is_data[0][1:]
Rev = is_data[1][1:]
CoR = is_data[2][1:]
GP = is_data[3][1:]
OE = is_data[4][1:]
OI = is_data[5][1:]
EPS = is_data[12][1:]
Exp = is_data[17][1:]

print(years)
print(Rev)
print(CoR)
print(GP)
print(EPS)
print(Exp)


# In[ ]:


stock = pe*eps


# In[13]:


import yfinance as yf

msft = yf.Ticker("MSFT")

# get historical market data (good)
#hist = msft.history(period="max")
#hist
# show financials (good)
#msft.financials
#msft.quarterly_financials

# show balance sheet 
#msft.balance_sheet
#msft.quarterly_balance_sheet

# show cashflow (good)
#msft.cashflow
#msft.quarterly_cashflow

# show earnings (good)
#msft.earnings
#msft.quarterly_earnings

# show analysts recommendations (good)
#msft.recommendations

# show next event (earnings, etc) (good)
#msft.calendar

# show news (good)
#msft.news


# In[ ]:




