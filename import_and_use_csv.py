#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:28:21 2019

@author: meixiangui
"""

import csv

% precision 2 

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
mpg[:3]

len(mpg)    
mpg[0].keys()
  
# average of the cty  
sum(float(d['cty'] for d in mpg)) / len(mpg)

sum(float(d['hwy'] for d in mpg)) / len(mpg)



# calculate the average of cyl by cty

cylinders = set(d['cyl'] for d in mpg)
cylinders 

CtyMpgByCyl = []

for c in cylinders: 
    summpg = 0 
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg+  = float(d['cty'])
            cyltypecount+ = 1
    CtyMpgByCyl.append((c, summpg / cyltypecount))
    
CtyMpgByCyl.sort(key = lambda x:x[0])  # sort by cylinders 
CtyMpgByCyl
    

# calculate the average of hwy by vehicle class
vehicleclass = set(d['class'] for d in mpg)
vehicleclass 

HwyMpgClass = []

for t in vehicleclass:
    summpg = 0 
    vclasscount = 0 
    for d in mpg:
        if d['class'] == t:
            summpg += float(d['hwy'])
            vclasscount+ = 1 
    HwyMpgByClass.append((t,summpg / vclasscount))
    
HwyMpgByClass.sort(key = lambda x:x[1])  # sort by hwy
HwyMpgByClass


    











