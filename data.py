#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


t_range = pd.date_range('2018-01-01', '2018-12-31', freq='H')


# In[3]:


t_range


# In[4]:


data_df = DataFrame(index=t_range)


# In[5]:


data_df.head


# In[6]:


data_df.head()


# In[7]:


data_df['Stomach'] = np.random.randint(0,10, size = len(t_range))


# In[8]:


data_df.head()


# In[9]:


data_df['Head'] = np.random.randint(0,30, size = len(t_range))


# In[10]:


data_df.head()


# # Unfiltered data

# In[11]:


data_df.plot()


# In[13]:


weekly_df = DataFrame()


# In[14]:


weekly_df['Stomach'] = data_df['Stomach'].resample('W').mean()


# In[15]:


weekly_df['Head'] = data_df['Head'].resample('W').mean()


# In[16]:


weekly_df.head()


# In[17]:


weekly_df.plot()


# In[37]:


filter_wdf = weekly_df[(weekly_df['Head'] > 5) & (weekly_df['Stomach'] < 4.5) ]


# In[38]:


filter_wdf


# #  Filtering data 

# In[39]:


filter_wdf.plot()


# In[40]:


type (filter_wdf)


# In[41]:


filter_wdf.plot(kind='bar')


# # The minimum

# In[43]:


weekly_df['Stomach'].sort_values()


# In[49]:


weekly_df['Head'].sort_values().head()


# In[56]:


wdf_head_min = weekly_df['Head'].min()


# In[57]:


wdf_head_min


# In[58]:


wdf_stomach_min = weekly_df['Stomach'].min()


# In[59]:


wdf_stomach_min


# # Mean

# In[51]:


wdf_mean = weekly_df['Stomach'].mean()


# In[52]:


wdf_mean


# In[54]:


wdf_mean_head = weekly_df['Head'].mean()


# In[55]:


wdf_mean_head


# # Average(median)

# In here, mean = average, so i get the median

# In[61]:


wdf_median_stomach= weekly_df['Stomach'].median()


# In[62]:


wdf_median_stomach


# In[63]:


wdf_median_head= weekly_df['Head'].median()


# In[64]:


wdf_median_head


# # Json

# In[69]:


data_df_json = data_df.to_json(orient='split')


# In[70]:


data_df_json


# In[71]:


json_load = json.loads(data_df_json)


# In[72]:


json_load


# In[ ]:




