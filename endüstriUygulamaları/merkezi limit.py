import matplotlib.pyplot as plt
import numpy as np

run=1000000
ortalamalar=np.zeros(run)
for k in range(run):
    ortalamalar[k]=np.random.poisson(10,size=(100)).mean()

print(ortalamalar.std())
plt.hist(ortalamalar,bins=1000)    
