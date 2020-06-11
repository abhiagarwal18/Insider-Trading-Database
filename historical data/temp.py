import pandas as pd

data = pd.read_csv('./final_data.csv')

data['BROADCASTE TIME'] = pd.to_datetime(data['BROADCASTE TIME'],format= '%H:%M' ).dt.time

data.to_csv('final_database.csv')