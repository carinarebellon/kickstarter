#!/usr/bin/env python
# coding: utf-8

# # This is for GA - Assignment
# 
# Author: Carina Rebellon
# Date: August 28, 2021

# In[24]:


#import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


# In[18]:


#load file
df = pd.read_csv ('C:\crebello\personal\GA\DSI_kickstarterscrape_dataset.csv')


# In[19]:


#drop columns not needed
df = df.drop(['name', 'url'], axis=1)
print(df)


# In[4]:


#profile the data
df.describe()


# In[5]:


#optional
df.fillna(value = {"pledged":0})

#get the mean 
df['pledged'].mean()


# In[6]:


plt.hist(df['backers'], bins=range(0,200,10))
plt.xlabel('Sum of Backers')
plt.ylabel('Count of Backers')
plt.title('Backers Distribution')
plt.show()


# In[43]:


print("mean of backers is : ", df['backers'].mean())
print("median of backers is : ", df['backers'].median())
print("mode of backers is : ",df['backers'].mode())

#positively skewed as Mean > Median


# # Duration Analysis

# In[21]:


plt.hist(df['duration'], bins=range(0,100,10))
plt.xlabel('Duration')
plt.ylabel('Count of Duration')
plt.title('Duration Distribution')
plt.show()


# In[45]:


print("mean of DUration is : ", df['duration'].mean())
print("median of DUration is : ", df['duration'].median())
print("mode of DUration is : ",df['duration'].mode())

#not normal, normal means mean, median and mode  are equal
#positively skewed as Mean > Median


# ***** sample code  to convert string to numeric ***********
# def success_to_numeric(x):
#         if x=='successful': return 0
#         if x=='live':   return 1
#         if x=='failed':   return 2
#         if x=='canceled':   return 3
#         if x=='suspended':   return 4
# 
#         
# df['status']   = df['status'].apply(success_to_numeric)
# 
# 
# print(df['status'])

# In[46]:


#using seaborn histogram to stacked the Status

sns.displot(df, x='duration', bins=20,hue="status",multiple="stack")


# In[47]:


#select duration and status 
df_duration = df[['duration', 'status']]

#filter success only
succ_df_by_dur = df_duration[df_cat['status'] == "successful"]

print("Mean of Duration for Success Status-",  succ_df_by_dur.mean())
print("Mode of Duration for Success Status-",  succ_df_by_dur.mode())
print("Median of Duration for Success Status-",  succ_df_by_dur.mean())


# In[42]:


#using seaborn histogram to stacked the Status

sns.displot(succ_df_by_dur, x='duration', bins=20,hue="status",multiple="stack", kde = True)


# # Qualitative - Goal

# In[61]:


sns.displot(df, x='goal', bins=range(0,100000,10000),hue="status",multiple="stack")

#goals below 20,000 have highest change of being successful


# In[48]:


#select category and status
df_goal = df[['goal', 'status']]

#filter success only
succ_df_by_dur = df_goal[df_cat['status'] == "successful"]

print("Mean of Goal for Success Status-",  succ_df_by_dur.mean())
print("Mode of Goal for Success Status-",  succ_df_by_dur.mode())
print("Median of Goal for Success Status-",  succ_df_by_dur.median())


# # Category Analysis

# In[52]:


#select category and status
df_cat = df[['category', 'status']]

#filter success only
succ_df_by_cat = df_cat[df_cat['status'] == "successful"]
failed_df_by_cat = df_cat[df_cat['status'] == "failed"]

#aggregate by category
succ_cat_summ = succ_df_by_cat.groupby(['category']).count().sort_values(by=['status'])
failed_cat_summ = failed_df_by_cat.groupby(['category']).count().sort_values(by=['status'])


# In[65]:


result = pd.merge(succ_cat_summ, failed_cat_summ, on="category",how="outer")
result = result.rename(columns={'status_x': 'Successful', 'status_y': 'Failed'})


# In[66]:


print(result)


# In[ ]:




