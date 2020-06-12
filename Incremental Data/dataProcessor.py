import pandas as pd
import os
import glob
from sqlPipeline import cleanerSaver

def preprocess(download_path):
    path = download_path
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    result = sorted(result,reverse = True)
    data = pd.read_csv(result[0])
    print(data.columns)
    data = data[['SYMBOL \n', 'COMPANY \n',  'NAME OF THE ACQUIRER/DISPOSER \n', 'CATEGORY OF PERSON \n', '% SHAREHOLDING (PRIOR) \n', 'NO. OF SECURITIES (ACQUIRED/DISPLOSED) \n', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n', 'ACQUISITION/DISPOSAL TRANSACTION TYPE \n', 'TYPE OF SECURITY (POST) \n', 'NO. OF SECURITY (POST) \n',  'MODE OF ACQUISITION \n','BROADCASTE DATE AND TIME \n']]
    
    df.rename({'SYMBOL \n': 'SYMBOL', 'COMPANY \n': 'COMPANY','NAME OF THE ACQUIRER/DISPOSER \n':'NAME OF THE ACQUIRER/DISPOSER','CATEGORY OF PERSON \n':'CATEGORY OF PERSON','% SHAREHOLDING (PRIOR) \n':'% SHAREHOLDING (PRIOR)','NO. OF SECURITIES (ACQUIRED/DISPLOSED) \n':'NO. OF SECURITIES (ACQUIRED/DISPLOSED)', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n':'VALUE OF SECURITY (ACQUIRED/DISPLOSED)','ACQUISITION/DISPOSAL TRANSACTION TYPE \n':'ACQUISITION/DISPOSAL TRANSACTION TYPE','TYPE OF SECURITY (POST) \n':'TYPE OF SECURITY (POST)', 'NO. OF SECURITY (POST) \n':'NO. OF SECURITY (POST)','MODE OF ACQUISITION \n':'MODE OF ACQUISITION','BROADCASTE DATE AND TIME \n':'BROADCASTE DATE AND TIME'}, axis=1, inplace=True)

    # sort the dataframe

    data.sort_values("SYMBOL", axis = 0, ascending = True, inplace = True, na_position ='last') 
    data.reset_index(drop=True, inplace=True)  
    cleanerSaver(data) 
    




