# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:29:36 2022

@author: LENOVO

merkezi limit teoreminin simülasyonu
"""
import numpy as np
from matplotlib import pyplot as plt

sample_size = 30
run = 10_000
means = np.zeros(run)

for i in range(run):
    means[i] = np.random.uniform(10,20,size=(sample_size)).mean()

plt.hist(means,bins=1000)
print("standart sapma : ",means.std())




