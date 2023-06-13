import numpy as np
p=10
c=3
s=1
cu=p-c
co=c-s
donem=50000
stok=np.zeros(donem)
satıs=np.zeros(donem)
yoksatma=np.zeros(donem)
maliyet=np.zeros(donem)
demand=np.random.normal(20,6,donem)
OTM=np.zeros(30)
for s in range(30):
    q=s
    for k in range(donem):
        if demand[k]>q:
            stok[k]=0
            satıs[k]=q
            yoksatma[k]=demand[k]-q
            maliyet[k]=cu*yoksatma[k]
        else:
            stok[k]=q-demand[k]
            satıs[k]=demand[k]
            maliyet[k]=co*stok[k]
        
    OTM[s]=sum(maliyet)/donem
print(OTM)
            