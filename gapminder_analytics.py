#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv('/Applications/Projects/Advanced_python/data/gapminder.tsv',sep='\t')


# In[15]:


df.head()


# In[16]:


df.shape 
#shape is an attribute of the datafrand and not a function of method


# In[19]:


df.columns  # lists of features 


# In[20]:


df.dtypes      # list columns and data types 


# In[21]:


df.info()


# In[24]:


country_df = df['country']       # assign data frame 
country_df.head()               # head by default list the first 5 items in the list 


# In[25]:


country_df.tail()     # tail by default list the last 5 items in the list 


# In[31]:


subset = df[['country','continent','year']]    # subset of the data in list form
subset.head()


# In[30]:


subset.tail(10)


# In[34]:


small_range = list(range(5))


# In[37]:


# we can use the .loc method on the DF to subset rows based on the index label
subset = df.loc[0]   # will give all of the information for first element of the column with is Afghanistan
# if you wanted to get the data for the 1703 only you would .loc(1703)   


# In[36]:


subset


# In[41]:


# to get information of 100th
df.loc[99]


# In[42]:


df.iloc[-1]   # gives the last row of the information


# In[43]:


df.loc[[0,99,999]]     # creates in List form


# In[44]:


df.iloc[[0,99,999]]


# In[49]:


pd.__version__


# In[50]:


df.loc[99,'country']


# In[51]:


df.iloc[99,0]


# In[53]:


df.head(n=10)


# In[55]:


df.head(100)


# In[56]:


df.groupby('year')['lifeExp'].mean()


# In[57]:


df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()


# In[62]:


df.groupby('continent')['country'].nunique()


# In[64]:


df.groupby('continent').head()


# In[ ]:




