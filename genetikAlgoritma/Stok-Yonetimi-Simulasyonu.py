# -*- coding: utf-8 -*-
"""

STOK YÖNETİMİ SİMÜLASYONU

@author : Muhammet Fettah Koral
"""
import json
import random as rd
import numpy as np

yeniden_siparis_noktasi=[10,11,12,13,14,15,16,17,18,19,20]
maximum_kapasite=[20,25,30,35,40,45]
tum_durumlar=[]

# q=40
# r=15

b=4
h=1
A=30

yoksatma_maliyeti=list()
stok_maliyeti=list()
siparis_maliyeti=list()
donem_basina_ort_maliyet=list()
toplam_maliyet=0

yoksatma=[]
stok=[]
siparis=[]
talep=[]
donem=100_000
lead_time = np.random.randint(3,6)


for q in maximum_kapasite:

    for r in yeniden_siparis_noktasi:
      
        stok.append(20)
        
        for k in range(donem):
            talep.append(rd.randint(10, 20))
            if talep[k]>stok[k]:
                stok[k]=0
                yoksatma.append(talep[k]-stok[k])
                yoksatma_maliyeti.append(yoksatma[k]*b)
                stok_maliyeti.append(0)
            else:
                stok[k]-=talep[k]
                stok_maliyeti.append(stok[k]*h)
                yoksatma.append(0)
                yoksatma_maliyeti.append(0)
            
            if r>=stok[k]:
                siparis.append(q-stok[k])
                siparis_maliyeti.append(A)
                if lead_time==0:
                    stok.append(stok[k]+siparis[k])
                    lead_time=np.random.randint(3,6)
                lead_time-=1
                stok.append(0)
            else :
                stok.append(stok[k])
                siparis.append(0)
                siparis_maliyeti.append(0)
        
            toplam_maliyet+=(stok_maliyeti[k]+yoksatma_maliyeti[k]+siparis_maliyeti[k])
            donem_basina_ort_maliyet.append(toplam_maliyet/(k+1))
            
        print("Q=",q," r=",r ," icin dönem başına ort. maliyet : ",
              donem_basina_ort_maliyet[donem-1])
        
        data={"Q":q,
              "r":r,
              "db_ort_maliyet":donem_basina_ort_maliyet[donem-1],
              "toplam_maliyet":toplam_maliyet}
        
        tum_durumlar.append(data)
        
        
        yoksatma.clear()
        stok.clear()
        siparis.clear()
        talep.clear()
        yoksatma_maliyeti.clear()
        stok_maliyeti.clear()
        donem_basina_ort_maliyet.clear()
        toplam_maliyet=0



print("\n########################################\n")

ortalama_maliyetler=[]

for item in tum_durumlar:
    ortalama_maliyetler.append(item["db_ort_maliyet"])

index=ortalama_maliyetler.index(min(ortalama_maliyetler))
print("en düşük ortalma maliyet : \n",tum_durumlar[index])





