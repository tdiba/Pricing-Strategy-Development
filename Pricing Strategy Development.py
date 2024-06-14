#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### Market Analysis

# In[2]:


# Load Market Analysis Data
market_analysis_df=pd.read_csv(r"C:\Users\USER\Documents\Data Portfolio Projects\Retail\Pricing Strategy Development\Datasets\Market_Analysis.csv")
market_analysis_df.head()


# In[3]:


#Plot share Distribution

import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# Plotting market share distribution

plt.figure(figsize=(10, 6))
sns.barplot(x='Market Share (%)', y='Competitor Name', data=market_analysis_df, palette='coolwarm')
plt.title('Market Share Distribution Among Competitors')
plt.xlabel('Market Share (%)')
plt.ylabel('Competitor')
plt.show()


# In[5]:


# Plotting price vs market share
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Market Share (%)', hue='Competitor Name', data=market_analysis_df, s=100)
plt.title('Price vs. Market Share Among Competitors')
plt.xlabel('Price ($)')
plt.ylabel('Market Share (%)')
plt.grid(True)
plt.show()


# In[ ]:





# ### Customer Segmentation

# In[7]:


#Load Customer Segmentation data
customer_segmentation_df=pd.read_csv(r"C:\Users\USER\Documents\Data Portfolio Projects\Retail\Pricing Strategy Development\Datasets\Customer_Segmentation.csv")
customer_segmentation_df.head()


# In[8]:


# Plot distribution of customers by age group
plt.figure(figsize=(8, 5))
sns.countplot(x='Age Group', data=customer_segmentation_df, palette='pastel')
plt.title('Distribution of Customers by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.show()


# In[9]:


# Visualization of buying frequency and average spend per visit by pet type
plt.figure(figsize=(12, 6))
sns.boxplot(x='Pet Type', y='Average Spend per Visit', data=customer_segmentation_df)
plt.title('Average Spend per Visit by Pet Type')
plt.xlabel('Pet Type')
plt.ylabel('Average Spend per Visit ($)')
plt.grid(True)
plt.show()


# In[11]:


# Buying frequency and average spend per visit by pet type
plt.figure(figsize=(12, 6))
sns.boxplot(x='Pet Type', y='Average Spend per Visit', data=customer_segmentation_df)
plt.title('Average Spend per Visit by Pet Type')
plt.xlabel('Pet Type')
plt.ylabel('Average Spend per Visit ($)')
plt.grid(True)
plt.show()


# In[ ]:





# In[10]:


#Loading Cost Analysis Data
cost_analysis_df=pd.read_csv(r"C:\Users\USER\Documents\Data Portfolio Projects\Retail\Pricing Strategy Development\Datasets\Cost_Analysis.csv")
cost_analysis_df.head()


# In[13]:


# Calculation of total cost per unit of finished product
cost_analysis_df['Cost per Batch ($)'] = cost_analysis_df['Cost per Unit ($)'] * cost_analysis_df['Required Units per Batch']
total_cost_per_batch = cost_analysis_df['Cost per Batch ($)'].sum()
total_units_produced = cost_analysis_df['Required Units per Batch'].iloc[0]  # assuming all are same
total_cost_per_unit = total_cost_per_batch / total_units_produced


# In[14]:


cost_analysis_df


# In[15]:


total_units_produced


# In[16]:


total_cost_per_batch


# In[17]:


total_cost_per_unit


# In[ ]:





# In[18]:


# Visualization of cost breakdown
plt.figure(figsize=(10, 6))
sns.barplot(x='Ingredient', y='Cost per Batch ($)', data=cost_analysis_df, palette='Set2')
plt.title('Cost Breakdown per Batch')
plt.xlabel('Cost Component')
plt.ylabel('Total Cost per Batch ($)')
plt.show()


# In[19]:


total_cost_per_batch, total_cost_per_unit


# In[ ]:




