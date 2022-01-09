#!/usr/bin/env python
# coding: utf-8

# In[1]:


import financedatabase as fd
import json


# In[2]:


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


# In[3]:


for x in sectors:
    data = fd.select_equities(country='United States', sector = x)
    ticker = list(data.keys())

    # Specifying Ticker
    for x in range(1):
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


# In[ ]:




