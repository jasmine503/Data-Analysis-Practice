#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:19:38 2019

@author: meixiangui
"""

# Assignment 2 
################Part A######################

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# Question1 
# Which country has won the most gold medals in summer games?
def answer_one():
    return df[df['Gold']==max(df['Gold'])].index[0]
answer_one()


# Question2 
# Which country had the biggest difference between their summer and winter gold medal count?
def answer_two():
    return df[(df['Gold']-df['Gold.1'])== max(df['Gold']-df['Gold.1'])].index[0]
answer_two()


# Question3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
def answer_three():
    df1 = df[(df['Gold']>=1) & (df['Gold.1']>=1)]
    df1['rediff'] = (df1['Gold']-df1['Gold.1'])/df1['Gold.2']
    return df1[df1['rediff'] == max(df1['rediff'])].index[0]
answer_three()


# Question4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, 
# silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point.
def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    return pd.Series(df['Points'],index=df.index)
answer_four()


################Part B######################

census_df = pd.read_csv('census.csv')
census_df.head()

# Question5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
def answer_five():
    sum = census_df.groupby('STNAME').agg(['count']).CTYNAME
    return sum[sum['count']==max(sum['count'])].index[0]

answer_five()


# Question6
# Only looking at the three most populous counties for each state, what are the three most populous states 
# (in order of highest population to lowest population)? Use CENSUS2010POP.
def answer_six():
    copy = census_df[census_df['SUMLEV'] == 50]
    copy = copy.groupby(['STNAME']).apply(lambda x: x.sort_values(['CENSUS2010POP'],ascending = False))
    copy = copy.groupby(['STNAME']).head(3)
    state = copy.groupby(['STNAME']).CENSUS2010POP.sum().nlargest(3)
    return state.index.tolist()
answer_six()

def answer_six():
    return census_df[census_df['SUMLEV'] == 50].groupby(
    'STNAME')['CENSUS2010POP'].apply(
    lambda x: x.nlargest(3).sum()).nlargest(
    3).index.values.tolist()
answer_six()


# Question7
# Which county has had the largest absolute change in population within the period 2010-2015? 
# (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
def answer_seven():
    copy = census_df[census_df['SUMLEV'] == 50]
    copy['change'] = None 
    compare = copy[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    copy['change'] = compare.max(axis = 1) - compare.min(axis = 1)
    return copy[copy['change'] == max(copy['change'])]['CTYNAME'].tolist()[0]
answer_seven()


# Question8 
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', 
# and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
def answer_eight():
    mask = census_df['REGION'].isin([1,2]) & census_df['CTYNAME'].str.startswith('Washington') & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])
    data = census_df.loc[mask]
    return data[['STNAME','CTYNAME']]

answer_eight()














