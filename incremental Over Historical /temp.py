import pandas as pd 
data = pd.read_csv('Insider_historical.csv')
print(data.columns)
data.reset_index( inplace=True)
data.index.name = 'SINo'
data.drop('index', axis=1, inplace=True)

data.to_csv('temp.csv')