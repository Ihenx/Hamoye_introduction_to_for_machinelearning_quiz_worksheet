#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import numpy as np


# In[73]:


# import the data
df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv',encoding='latin-1')
df.head()


# ### 1. Which of the following dataframe methods can be used to access elements across rows and columns

# In[74]:


df.iloc[0:4,0:4]


# from the above dataframe, i was able to use the iloc pandas method to access the rows and columns of the dataframe.

# ### 2.Perform a groupby operation on 'Element': what is the total numberof the sum of processing in 2017

# In[75]:


element_df = df.groupby('Element')['Y2017'].sum()
element_df['Processing']


# ### 3. How would you check the number of  rows and columns in a pandas DataFrame named df?

# In[76]:


df.shape


# The above shows the dataframe has about 60943 rows and 12 columns

# ### 4. Select the columns 'Y2017' and Area. Perform a groupby operation on area. Which of these A had the 7 lowest sum in 2017

# In[77]:


df.groupby('Area')['Y2017'].sum().sort_values().head(7)


# In[78]:


## Alternatively
Y_2017_df=df.groupby('Area').agg({'Y2017':sum}).nsmallest(7,'Y2017')
Y_2017_df= Y_2017_df.idxmax()
Y_2017_df


# ### 5 Consider the following  list tuples
# 

# In[79]:


y = [(2,4),(7,8),(1,5,9)]
x=y[1][1]
x


# ### 6.What would the output of the following be?

# In[80]:


s = [['him','sell'],[90,28,43]]
s[0][1][1]


# ###  7.A pandas DataFrame with dimensions (100,3) has how many features and observations?
# 
# answer: this means the dataframe has about 100 obeservations(rows) and 3 features(columns)

# ### 8. 

# In[81]:


array = np.array([[94,89,63],[93,92,94],[92,94,96]])
array[:2,1:]


# ### 9. What is the total protein supply quantity in Madagascar in 2015

# In[82]:


## filter the madagascar from the  the Area column
madagascar_df = df[df['Area']=='Madagascar']


# In[83]:


madagascar_df=madagascar_df.groupby('Element')['Y2015'].sum()
madagascar_df['Protein supply quantity (g/capita/day)']


# ###  10. Which year had the least correlation with 'Element Code'

# In[84]:


df.corr()['Element Code'].sort_values()


# ###  11. What is the total number and percentage of missing data in 2014 to 3 decimal places?

# In[85]:


# find the total missing values in the dataFrame
total_missing = df.isnull().sum().sum()
total_missing


# In[86]:


# Find rthe total missing values in Y2014 column
y2014_missing=df.isnull().sum()
y2014_missing=y2014_missing['Y2014']


# In[87]:


# find the percentage of the missing value of each column
percentage_y2014_missing=round((df.isnull().sum()/total_missing) * 100,3)

# select the percentage of missing value in Y2014 using 
percentage_y2014_missing=percentage_y2014_missing.Y2014
percentage_y2014_missing


# In[88]:


print('{0} and {1}%'.format(y2014_missing,percentage_y2014_missing))


# In[ ]:





# ### 12 .Perform the groupby operation on Element

# In[89]:


''' create a list comprehension, looping through the df.columns.
    Since only the year column starts with the alphabet 'Y'.Include a a condition
    on the loop to select only the  columns that starts with 'Y' using the startswith
     function.
     
'''
year_columns = [col for col in df.columns if col.startswith('Y')]
year_columns


# In[90]:


element_df = df.groupby('Element')[year_columns].sum()
stock_variation_sum = element_df.loc['Stock Variation']
stock_variation_sum


# In[91]:


year_with_highest_sum_stock_variation =stock_variation_sum.idxmax()
year_with_highest_sum_stock_variation


# ### 13.  What is the total sum of wine produced in 2015 and 2018

# In[92]:


wine_df =df.groupby('Item')[['Y2015','Y2018']].sum()
wine_df.loc['Wine']


# ### 14. What is the total number of unique countries in the datasets
# 

# In[93]:


df.Area.nunique()


# In[94]:


#Alternatively
len(df.Area.unique())


# ### 15. Select columns 'Y2017' and 'Area'.Perform a groupby operation on the area.Which of these Area had the highest sum.

# In[95]:


y_2017_df = df.groupby('Area')['Y2017'].sum().sort_values(ascending=False)
print('{0} :{1}'.format(y_2017_df.idxmax(), y_2017_df.max()))


# ### 16. What would the output of the code below give?

# In[96]:


my_tuple = (1,2,5,8)
my_tuple[2]= 6


# The above error occurs because tuples are immutable. This means once the content of the tuple is declared, the content can no longer be modified.

# In[ ]:





# ### 17. What is  the mean and Standard deviation accross he whole data set for the whole year to 2 decimal places.

# In[97]:


y2017_mean=round(df.Y2017.mean(),2)
y2017_mean


# In[98]:


y2017_std= round(df.Y2017.std(),2)
y2017_std


# ###   18.

# In[102]:


lst = [[35,'Portugal',94],[33,'Argentina',93],[30,'Brazil',92]]
col = ['Age','Nationality','Overall']


# In[103]:


df = pd.DataFrame(lst,columns=col,index=[1,2,3])


# In[104]:


df


# In[ ]:





# In[ ]:




