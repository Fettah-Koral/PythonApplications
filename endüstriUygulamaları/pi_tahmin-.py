
import numpy as np
import matplotlib.pyplot as plt
run=100000
x=-1+2*np.random.rand(run,2)
uzaklık=np.sum(x**2,axis=1)
ind1=(uzaklık<=1)
ind2=(uzaklık>1)
plt.scatter(x[ind1,0],x[ind1,1])
plt.scatter(x[ind2,0],x[ind2,1])
plt.show()
pi_tahmin=4*(sum(ind1)/run)
print(pi_tahmin)
# print(uzaklık[ind1])
# print(uzaklık)

        
    