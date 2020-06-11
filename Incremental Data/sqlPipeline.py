import pandas as pd

def cleanerSaver(data):
    temp = []
    #print(data.columns)
    for item in data['NO. OF SECURITY (POST) \n']:
        if (str(item)) == 'Nil':
            item_v = str(0)
        else:
            item_v = item
        temp.append(item_v)
    data.loc[:, 'NO. OF SECURITY (POST) \n'] = temp 

    data['BROADCASTE DATE \n'], data['BROADCASTE TIME \n'] = data['BROADCASTE DATE AND TIME \n'].str.split(' ', 1).str
    data.drop(['BROADCASTE DATE AND TIME \n'], axis = 1, inplace = True) 
    print(data.info())
    
    data['BROADCASTE TIME'] = pd.to_datetime(data['BROADCASTE TIME'],format= '%H:%M' ).dt.time
    data.index.name = 'index'
    data.to_csv('final_database.csv')

''' testing run
data = pd.read_csv('./final_data.csv')
cleanerSaver(data)
'''