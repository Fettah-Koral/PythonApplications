 #1 -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:52:34 2022

@author: Muhammet Fettah Koral
"""

import numpy as np 
import matplotlib.pyplot as plt 

# pi / 4  = x / run  ==>  pi = 4.x / run

run = 100000

x = np.random.uniform(-1,1,size=(run,2))

distance = np.sum(x**2,axis=1)

ind1 = distance<=1
ind2 = distance>1

pi_pred = 4*sum(ind1) /run

plt.scatter(x[ind2,0],x[ind2,1])
plt.scatter(x[ind1,0],x[ind1,1])
plt.show()