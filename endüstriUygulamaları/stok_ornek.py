import random 
donem=1000
demand=list((random.randint(10,20),))
stok=[10]
satis=[]
yoksatma=[]
siparis=[]
q=100
r=50

for k in range(donem):
    # print(k)
    if demand[k] > stok[k]:
        satis.append(stok[k])
        yoksatma.append(demand[k]-stok[k])
        stok[k]=0
    else:
        satis.append(demand[k])
        stok[k]=stok[k]-demand[k]
        yoksatma.append(0) 
    
    if stok[k]<r:
       stok.append(q)
       siparis.append(q-stok[k])
    else:
       stok.append(stok[k])
       siparis.append(0)
       
    
    demand.append(random.randint(10,20))

print(satis)
