#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:06:56 2019

@author: meixiangui
"""

import pandas as pd
import numpy as np 

# Question 1
# Can you use method chaining to modify the DataFrame df in one statement to 
# drop any entries where 'Quantity' is 0 and rename the column 'Weight' to 'Weight (oz.)'?
print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))

# Question 2
# Use groupby to group the dataframe, and apply a function to 
# calculate the total weight (Weight x Quantity) by category.
df['Total_weight'] = df['Weight (oz.)']*df['Quantity']
print(df.groupby('Category')['Total_weight'].apply(lambda x: x.sum()))

print(df.groupby('Category').
      apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

def totalweight(df, w, q):
    return sum(df[w] * df[q])        
print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

# Question 3
# Try casting this series to categorical with the ordering Low < Medium < High.
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s = s.astype('category',categories = ['Low','Medium','High'], ordered = True)
print (s)

# Question 4
# Suppose we have a series that holds height data for jacket wearers.
# Use pd.cut to bin this data into 3 bins.
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

# Your code here
pd.cut(s, 3)
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

########Date Functionality in Pandas########
# Timestamp 
pd.Timestamp('9/1/2016 10:05AM')

# Period 
pd.Period('3/5/2016')   # Period('2016-03-05', 'D')
pd.Period('1/2016')     # Period('2016-01', 'M')

# Datetime Index 
t1 = pd.Series(list('abc'),[pd.Timestamp('2016-09-01'),pd.Timestamp('2016-09-02'),pd.Timestamp('2016-09-03')])
t1
type(t1.index)

# Period Index 
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
t2 
type(t2.index)

# Converting to Datetime 
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10,100,(4,2)), index = d1, columns = list('ab'))
ts3

ts3.index = pd.to_datetime(ts3.index)
ts3 

# specify day to be the first 
pd.to_datetime('4.7.12', dayfirst = True)

# Timedeltas 
pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')  # Timedelta('2 days 00:00:00')
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')  # Timestamp('2016-09-14 11:10:00')

# Working with dates in a Dataframe
# take biweekly, every Sunday and 9 measurements 
dates = pd.date_range('10-01-2016', periods = 9, freq = '2W-SUN')
dates

df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5,10,9).cumsum(),
                   'Count 2': 100 + np.random.randint(-5,10,9)}, index = dates)
df 
# check whether they are all Sunday 
df.index.weekday_name

# check diff 
df.diff()

# mean of each month 
df.resample('M').mean()

df['2017']
df['2016-12']
df['2016-12':]

# change frequency to each week 
df.asfreq('W', method = 'ffill')

# plot the time series 
import matplotlib.pyplot as plt
%matplotlib inline 

df.plot()














