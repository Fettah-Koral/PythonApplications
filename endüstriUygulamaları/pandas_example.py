import pandas as pd
import numpy as np
import random
student=[]
gender=[]
vize1=[]
vize2=[]
final=[]
adres=[]
for k in range(100):
    student.append('student'+str(k+1))
    gender.append(random.choice(['Male','Female']))
    vize1.append(random.randint(30,100))
    vize2.append(random.randint(30,100))
    final.append(random.randint(30,100))
    adres.append(random.choice(['Kayseri','İstanbul','Ankara']))

data={'student':student,'gender':gender,'adres':adres,
                 'vize1':vize1,'vize2':vize2,'final':final}
df=pd.DataFrame(data,index=[student])

df1=pd.DataFrame(df,columns=['gender','final'])
df2=pd.DataFrame(df,columns=['gender','vize3','final'])
print(df2)
df.head()
df.tail()
print(df1.final.mean())
print(df.gender.unique())
print(df.gender.value_counts())
print(df.final.plot(kind='hist'))
print(df.final.value_counts().plot(kind='bar'))

df.loc[['student1']]
print(df.iloc[3:8]['final'])

df2.vize3=np.arange(0,100)

del df2['vize3']
df2.index.name='ogrenci'
df2.columns.name='notlar'
print(df2)