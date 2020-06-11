import pandas as pd

data = pd.read_csv('final_historical_data.csv')
#print(data.info())


#data['NO. OF SECURITY (POST)'].astype(str)
temp = []
for item in data['NO. OF SECURITY (POST)']:
    if (str(item)) == 'Nil':
        item_v = str(0)
    else:
        item_v = item
    temp.append(item_v)
data.loc[:, 'NO. OF SECURITY (POST)'] = temp 

data['BROADCASTE DATE'], data['BROADCASTE TIME'] = data['BROADCASTE DATE AND TIME'].str.split(' ', 1).str



print(data.info())




data.to_csv('temp.csv', index = False)

