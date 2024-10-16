#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re


# In[30]:


data=pd.read_csv('titanic.csv')
data.head()


# In[18]:


data.isna().sum()


# In[5]:


#filling null values
data['Age'].fillna(data['Age'].mean(),inplace=True)


# In[6]:


data['Fare'].fillna(data['Fare'].mean(),inplace=True)


# In[7]:


#using 1 hot encoding to convert categorical variables
data['Sex']=data['Sex'].map({'male':0,'female':1})


# In[8]:


data['Embarked']=data['Embarked'].map({'S':0,'Q':1,'C':2})


# In[9]:


data.isna().sum()


# In[10]:


data.head()


# In[11]:


#min-max scaling transform
data['Age']=(data['Age']-data['Age'].min())/(data['Age'].max()-data['Age'].min())


# In[12]:


data.head()


# In[13]:


#z-score scaling transform
data['Fare']=abs(data['Fare']-data['Fare'].mean())/data['Fare'].std()


# In[14]:


data.head()


# In[41]:


df=pd.read_csv('customers.csv')


# In[21]:


df.head()


# In[42]:


df=df.drop(['Unnamed: 0','market_place','customer_id','product_parent','product_category','helpful_votes','total_votes','vine','review_month','review_day','review_year'],axis=1)


# In[33]:


df


# In[43]:


cols = ['review_id','product_id','product_title','review_headline','review_body']
for i in cols:
    df[i] = df[i].str.replace('"','',regex=False)


# In[44]:


df



# In[46]:


cols=['product_title','review_headline','review_body','verified_purchase']
for c in cols:
     df[c] = df[c].fillna('').str.replace(r'[;,.!?:()"+#</>]|', '', regex=True)
df
df['verified_purchase'] = df['verified_purchase'].str.replace(r'\tY+', '', regex=True)
df['verified_purchase'] = df['verified_purchase'].str.replace(r'\tN+', '', regex=True)
df


# In[ ]:




