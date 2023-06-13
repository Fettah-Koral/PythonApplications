# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:42:56 2022

@author: LENOVO
"""

import numpy as np

p=10  # price
c=5.5 # unit cost
s=1  # salvage
cu = p-c # under cost
co = c-s # over cost 
donem = 100_000
talep = np.random.normal(20,4,size=(donem))

stok = np.zeros(donem)
satis = np.zeros(donem)
yok_satma = np.zeros(donem)
maliyet = np.zeros(donem)

Q = np.arange(10,30)
AC = np.zeros(len(Q))

for j in range(len(Q)):
    
    q = Q[j]
    
    for k in range(donem):
        if q > talep[k]:
            stok[k] = q - talep[k]
            satis[k] = talep[k]
            yok_satma[k] = 0
            maliyet[k] = co * stok[k]
            
        else:
            stok[k] = 0
            satis[k] = q
            yok_satma[k] = talep[k] - q
            maliyet[k] = cu * yok_satma[k]
            
    AC[j] = sum(maliyet) / donem
    print(AC[j])

print("-----------"*4)
print("\nbest solve ==>  %d"%(np.argmin(AC)),".observation  : ",AC[np.argmin(AC)])
    
    
    