import random 
donem=100000

h=1
b=3
A=400
R=list(range(5,10,1))
Q=list(range(50,150,10))
for i in range(len(R)):
    r=R[i]
    for j in range(len(Q)):
        demand=list((random.randint(10,20),))
        stok=[10]
        satis=[]
        yoksatma=[]
        siparis=[]
        q=Q[j]
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
        
            
        sip=[item>0 for item in siparis]
        sipM=A*sum(sip)
        stokM=h*sum(stok)
        yokM=b*sum(yoksatma)
        TM=(sipM+stokM+yokM)/donem
        
        print("r={}, q={}, TM={}".format(r,q,TM))
       
        





