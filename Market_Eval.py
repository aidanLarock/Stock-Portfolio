#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import fmean, variance

from datetime import datetime, timedelta
import requests
from lxml import html as HTMLParser


# In[2]:


# Calculates P/E, Shiller P/E, Interest Rates, Dividend Yields of months specified over S&P 500
# Uses Mean, Varience to calculate closness to standard
# Outputs Value from 0-99 of under to over valued

Months = 12


# In[3]:


# P/E

pe_url = 'http://www.multpl.com/table?f=m'

def get_data_from_multpl_website(url):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        )
    }
    res = requests.get(url, headers=headers)
    parsed = HTMLParser.fromstring(res.content.decode('utf-8'))
    tr_elems = parsed.cssselect('#datatable tr')
    raw_data = [[td.text.strip() for td in tr_elem.cssselect('td')] for tr_elem in tr_elems[1:]]
    return raw_data


pe_data = get_data_from_multpl_website(pe_url)


# In[4]:


# Shiller P/E

pe_url = 'https://www.multpl.com/shiller-pe/table/by-month'

def get_data_from_multpl_website(url):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        )
    }
    res = requests.get(url, headers=headers)
    parsed = HTMLParser.fromstring(res.content.decode('utf-8'))
    tr_elems = parsed.cssselect('#datatable tr')
    raw_data = [[td.text.strip() for td in tr_elem.cssselect('td')] for tr_elem in tr_elems[1:]]
    return raw_data


shiller_data = get_data_from_multpl_website(pe_url)


# In[5]:


# Interest Rates

pe_url = 'https://www.multpl.com/5-year-real-interest-rate/table/by-month'

def get_data_from_multpl_website(url):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        )
    }
    res = requests.get(url, headers=headers)
    parsed = HTMLParser.fromstring(res.content.decode('utf-8'))
    tr_elems = parsed.cssselect('#datatable tr')
    raw_data = [[td.text.strip() for td in tr_elem.cssselect('td')] for tr_elem in tr_elems[1:]]
    return raw_data


int_data = get_data_from_multpl_website(pe_url)


# In[6]:


# Dividend Yeilds

pe_url = 'https://www.multpl.com/s-p-500-dividend-yield/table/by-month'

def get_data_from_multpl_website(url):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        )
    }
    res = requests.get(url, headers=headers)
    parsed = HTMLParser.fromstring(res.content.decode('utf-8'))
    tr_elems = parsed.cssselect('#datatable tr')
    raw_data = [[td.text.strip() for td in tr_elem.cssselect('td')] for tr_elem in tr_elems[1:]]
    return raw_data


div_data = get_data_from_multpl_website(pe_url)


# In[7]:


div_data = np.array(div_data[:Months])
int_data = np.array(int_data[:Months])
shiller_data = np.array(shiller_data[:Months])
pe_data = np.array(pe_data[:Months])

div_data = div_data[:,1]
int_data = int_data[:,1]
shiller_data = shiller_data[:,1]
pe_data = pe_data[:,1]


# In[8]:


PE = [float(i) for i in pe_data]
SHIL = [float(i) for i in shiller_data]
INT = [float(i.strip('%')) for i in int_data]
DIV = [float(i.strip('%')) for i in div_data]


# In[9]:


# P/E Data

avg = fmean(PE)
var = variance(PE, avg)
cur = PE[0]

print(avg)
print(var)
print(cur)


# In[10]:


# SHILLER P/E Data

avg = fmean(SHIL)
var = variance(SHIL, avg)
cur = SHIL[0]

print(avg)
print(var)
print(cur)


# In[11]:


# DIVIDEND YIELD Data

avg = fmean(DIV)
var = variance(DIV, avg)
cur = DIV[0]

print(avg)
print(var)
print(cur)


# In[12]:


# INTEREST RATES Data

avg = fmean(INT)
var = variance(INT, avg)
cur = INT[0]

print(avg)
print(var)
print(cur)


# In[ ]:




