#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:58:20 2019

@author: meixiangui
"""

import numpy as np

# Question 1
# Suppose we want to simulate the probability of flipping a fair coin 20 times, and getting a number greater than or equal to 15. 
# Use np.random.binomial(n, p, size) to do 10000 simulations of flipping a fair coin 20 times, 
# then see what proportion of the simulations are 15 or greater. 
x = np.random.binomial(20, .5, 10000) # 10000 is simulation 
print((x>=15).mean())

# Question 2 
# Simulate the real world
chance_of_tornado = 0.01 / 100
np.random.binomial(100000, chance_of_tornado)

chance_of_tornado = 0.01
tornado_events = np.random.binomial(1,chance_of_tornado, 100000)

two_days_in_a_row = 0 
for j in range(1,len(tornado_events)-1):
    if tornado_events[j] == 1 and tornado_events[j-1] == 1: 
        two_days_in_a_row += 1
        
print('{} tornadoes back to back in {} years'. format(two_days_in_a_row, 100000/365))


distribution = np.random.normal(0.75, size = 1000)
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))
np.std(distribution)

# Skewness of the distribution 
import scipy.stats as stats

chi_squared_df2 = np.random.chisquare(2, size = 10000)
stats.skew(chi_squared_df2)

chi_squared_df5 = np.random.chisquare(5, size = 10000)
stats.skew(chi_squared_df5)


S0 = 25
K = 28
T = 1
sim = 10**3
steps = 252
sigma = 0.4
r = 0.02

def asian(S0,path, step, sigma,r, T, K):
    dt = T/step 
    dwt = np.random.normal(size = step*path).reshape(path, step)* np.sqrt(dt)
    #dwt = np.random.randn(path,step)*np.sqrt(dt)
    mul = np.log(S0)+np.cumsum((r-0.5*sigma**2)*dt+ sigma*dwt, axis = 1)
    s = np.exp(mul)
    s_new = s[:,-30::1].mean(1)
    
    call = np.mean(np.maximum(s_new -K, 0)) * np.exp(-r*T)
    
    return call
    
asian(25,100000, 252, 0.4, 0.02, 1, 28 ) 

T = 1
step = 252
path = 10000
r = 0.02
sigma = 0.4
S0 = 25
K = 28 


