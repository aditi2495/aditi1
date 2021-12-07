#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[3]:


df


# In[4]:


df[['FlightNumber']] = df[['FlightNumber']].astype('Int64')


# In[5]:


df[['FlightNumber']]


# In[6]:


df.loc[df['FlightNumber'].isna(),'FlightNumber'] = df.loc[df[df['FlightNumber'].isna()].index-1,'FlightNumber'].astype(int)+10


# In[7]:


df


# In[8]:


df['From_To']


# In[9]:


df[['From']] = df['From_To'].str.split('_', expand=True)[0]
df[['To']] = df['From_To'].str.split('_',expand = True)[1]


# In[10]:


df


# In[11]:


df['From'] = df['From'].str.capitalize()


# In[12]:


df


# In[17]:


df.drop('From_To',axis = 1, inplace =True)


# In[18]:


df


# In[ ]:




