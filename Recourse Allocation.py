#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import pickle
import requests
import math


# In[2]:


# Allocation 
# Output Recourse Allocation

# 0 - 99 Market Eval Calculations
IN = 20
num_Stock = 100


# In[3]:


def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[3].text
        tickers.append(ticker)
        
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    return tickers

industry = save_sp500_tickers()


# In[4]:


HEC = industry.count('Health Care')
IND = industry.count('Industrials')
INT = industry.count('Information Technology')
COM = industry.count('Communication Services')
COND = industry.count('Consumer Discretionary')
UTL = industry.count('Utilities')
FNC = industry.count('Financials')
RES = industry.count('Real Estate')
MAT = industry.count('Materials')
CONS = industry.count('Consumer Staples')
ENG = industry.count('Energy')

INT = INT + ENG + RES

Total = INT + HEC + IND + COM + COND + UTL + FNC + MAT + CONS


# In[5]:


#Sectors (S&P)
sectors = {
    'Technology': INT/Total,
    'Services': UTL/Total,
    'Basic Materials': MAT/Total,
    'Industrials': IND/Total,
    'Healthcare':  HEC/Total,
    'Financial Services': FNC/Total,
    'Consumer Defensive': CONS/Total,
    'Consumer Cyclical': COND/Total,
    'Communication Services': COM/Total
}


# In[6]:


#Stock Caps (billion)
small = 0,2
medium = 2,10
large = 10

#Portfolio Types (Eq,Cash,Sec)
M_Con = 40,20,40
Con = 25,40,35
v_Con = 10,60,30
M_Agg = 55,10,35
Agg = 75,5,20
v_Agg = 90,5,5

if(IN >= 85 and IN <= 100):
    Chosen = V_Con
if(IN >= 74 and IN <= 85):
    Chosen = Con
if(IN >= 58 and IN <= 74):
    Chosen = M_Con
if(IN >= 41 and IN <= 57):
    Chosen = M_Agg
if(IN >= 21 and IN <= 40):
    Chosen = Agg
if(IN >= 0 and IN <= 20):
    Chosen = v_Agg

#chosen strategy
print(Chosen)


# In[7]:


for x in sectors:
    # value of stock using type
    val = (sectors[x])*Chosen[0]
    print("Sector: "+ x +" "+ str(int(val))+"%")


# In[8]:


# Using Chosen Strategy (Agg = 60% Stock)
for x in sectors:
    # value of stock using type
    val = (sectors[x])*Chosen[0]
    print("Sector Stocks: "+ x +" = "+ str(int(val)))

