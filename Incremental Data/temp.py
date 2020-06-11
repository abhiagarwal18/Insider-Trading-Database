import pandas as pd

data = pd.read_csv('./final_database.csv')

data['BROADCASTE TIME \n'] = pd.to_datetime(data['BROADCASTE TIME \n'],format= '%H:%M' ).dt.time

data.to_csv('temp.csv')