import pandas as pd

data = pd.read_csv('./test_data.csv')

data['BROADCASTE TIME \n'] = pd.to_datetime(data['BROADCASTE TIME \n'],format= '%H:%M' ).dt.time
data.index.name = 'index'

data.to_csv('final_data.csv')