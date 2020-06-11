import pandas as pd

data = pd.read_csv('./tester.csv')

data['BROADCASTE TIME'] = pd.to_datetime(data['BROADCASTE TIME'],format= '%H:%M' ).dt.time
data.index.name = 'index'
data.to_csv('final_database.csv')