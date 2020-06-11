import pandas as pd
    
def cleanerSaver(data):
    temp = []
    for item in data['NO. OF SECURITY (POST)']:
        if (str(item)) == 'Nil':
            item_v = str(0)
        else:
            item_v = item
        temp.append(item_v)
    data.loc[:, 'NO. OF SECURITY (POST)'] = temp 
    data.to_csv('final_data.csv', index = False)
'''
    data['BROADCASTE DATE'], data['BROADCASTE TIME'] = data['BROADCASTE DATE AND TIME'].str.split(' ', 1).str
    data.drop(['BROADCASTE DATE AND TIME'], axis = 1, inplace = True) 
    print(data.info())
    data.index.name = 'index'''
    
    

data = pd.read_csv('./final_historical_data.csv')
cleanerSaver(data)