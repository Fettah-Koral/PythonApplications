import pandas as pd
df=pd.read_csv('covid-daywise.csv')
print(type(df))
print(df.info())
print(df.head())
print(df.describe())
print(df.columns)
print(df.shape)
covid_data_sozluk = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1130, 1665, 1234, 2115, 965],
    'new_deaths': [1, 2, 2, 2, 3],
    'new_tests': [63934, 36593, 54625, None, None]
}

print(covid_data_sozluk['date'])
print(df['new_cases'])
print(type(df['new_cases']))
print(df['new_cases'][100])
print(df.at[100,'new_cases'])
print(df.new_cases)
print(df[['new_cases','date']])
df_copy=df
print(df.loc[200])
print(df.head(5))
print(df.tail(4))
print(df.new_tests.first_valid_index())
print(df.loc[108:113])
print(df.sample(5))

total_cases=df.new_cases.sum()
total_deaths=df.new_deaths.sum()
oran=total_deaths/total_cases
print('toplam olum oranı % {} dir'.format(round(oran*100,2)))

y_vakalar=df.new_deaths>300
df[y_vakalar]

df['year']=pd.DatetimeIndex(df.date).year
df['month']=pd.DatetimeIndex(df.date).month
df['day']=pd.DatetimeIndex(df.date).day
df['weekday']=pd.DatetimeIndex(df.date).weekday

covid_mart=df[df.month==3]
print(covid_mart.sample(5))
print(covid_mart[['new_cases','new_deaths']])
print(df[df.month==3]['new_cases'].mean())