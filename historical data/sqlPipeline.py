import pandas as pd
from importToSQL import createSQLdatabase  
def cleanerSaver(data):
    temp = []
    for item in data['NO. OF SECURITY (POST)']:
        if (str(item)) == 'Nil':
            item_v = str(0)
        else:
            item_v = item
        temp.append(item_v)
    data.loc[:, 'NO. OF SECURITY (POST)'] = temp 
    data.drop_duplicates()

    deleterows = []
    for index, row in data.iterrows():
        if(row['% SHAREHOLDING (PRIOR)']==0 and row['VALUE OF SECURITY (ACQUIRED/DISPLOSED)']== '-' and row['ACQUISITION/DISPOSAL TRANSACTION TYPE']== '-' ):
            deleterows.append(index)
        else :
            pass
    
    data.drop(data.index[deleterows], inplace=True)
    data.reset_index( inplace=True)
    data.index.name = 'Index'
    data.to_csv('final_data_Jun12_7pm.csv', index = False)
    createSQLdatabase(data)
'''
    data['BROADCASTE DATE'], data['BROADCASTE TIME'] = data['BROADCASTE DATE AND TIME'].str.split(' ', 1).str
    data.drop(['BROADCASTE DATE AND TIME'], axis = 1, inplace = True) 
    print(data.info())
    data.index.name = 'index'''
    

#TESTING FUNCTION CALLS

# data = pd.read_csv('./tester.csv')
# cleanerSaver(data)