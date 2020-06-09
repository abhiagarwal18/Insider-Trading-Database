import pandas as pd
import os
import glob


def preprocess(download_path):
    path = download_path
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    result = sorted(result,reverse = True)
    data = pd.read_csv(result[0])
    print(data.columns)
    data = data[['SYMBOL \n', 'COMPANY \n',  'NAME OF THE ACQUIRER/DISPOSER \n', 'CATEGORY OF PERSON \n', '% SHAREHOLDING (PRIOR) \n', 'NO. OF SECURITIES (ACQUIRED/DISPLOSED) \n', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n', 'ACQUISITION/DISPOSAL TRANSACTION TYPE \n', 'TYPE OF SECURITY (POST) \n', 'NO. OF SECURITY (POST) \n',  'MODE OF ACQUISITION \n','BROADCASTE DATE AND TIME \n']]
    # sort the dataframe
    data.sort_values("SYMBOL \n", axis = 0, ascending = True, inplace = True, na_position ='last') 
    data.reset_index(drop=True, inplace=True)
    data.to_csv('final_data.csv', index = False)    
    




