import random
genislik=4
sayı=random.sample(range(10),genislik)
# print(sayı)

while True:
    guess=input("{} rakamlı bir sayı giriniz: ".format(genislik))
    tahmin=[]
    for k in guess:
        tahmin.append(int(k))
    
    if tahmin==sayı:
        print("\tBravo, bildiniz!!!! Sayılar eşleşti")
        break
          
    if len(tahmin)!=genislik:
        print("sayı genisligi aynı olması gerekir")
        continue
    
    sonuc=''
    c_tahmin=tahmin.copy()
    c_sayı=sayı.copy()
    for i in range(genislik):
        if c_tahmin[i]==c_sayı[i]:
            sonuc=sonuc+'*'
            c_tahmin[i]='_'
            c_sayı[i]='_'
    print(sonuc)
    
    for i in range(genislik):
        if c_tahmin[i]=='_':
            continue
        
        if c_tahmin[i] in c_sayı:
            sonuc=sonuc+'+'
            
    sonuc=list(sonuc)
    print(sonuc)
