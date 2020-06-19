#Primary file :
#To be used to append incremental data to the historical database in the SQL table 


import pandas as pd
from selenium import webdriver
import glob
import os
import time
import pyodbc

''' LIST OF PATHS TO BE ADDED: 
PATH1. prefs - download directory
eg.
/Users/abhishek/Desktop/Insider-Trading-Database/incremental Over Historical  (MAC/LINUX)
C:\\Users\\hritw\\Desktop\\incremental Over Historical\\incremental Over Historical (WINDOWS)

PATH2. chrome_path - chromedriver path
eg.
/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/chromedriver
C:\\Users\\hritw\\Downloads\\chromedriver_win32\\chromedriver.exe

PATH3. path - directory with the codes; same as the path in 1.
eg.
/Users/abhishek/Desktop/Insider-Trading-Database/incremental Over Historical 
C:\\Users\\hritw\\Desktop\\incremental Over Historical\\incremental Over Historical

PATH4. original file - downloadDirectory/filename
eg. 
C:\\Users\\hritw\\Desktop\\incremental Over Historical\\incremental Over Historical\\Insider_historical.csv
/Users/abhishek/Desktop/Insider-Trading-Database/incremental Over Historical/Insider_historical.csv

THE DETAILS REGARDING SQL SERVER-RELATED PATHS AND CONNECTIONS NEED TO BE UPDATED AS PER LOCAL/REMOTE SERVER
'''


#chromedriver details

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\\Users\\hritw\\Desktop\\incremental Over Historical\\incremental Over Historical'}
chrome_options.add_experimental_option('prefs', prefs)
chrome_path = "C:\\Users\\hritw\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path, options=chrome_options)

#removing redundant files
extension = 'csv'
path = "C:\\Users\\hritw\\Desktop\\incremental Over Historical\\incremental Over Historical"


for filename in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension)):
   os.remove(filename) 

#downloading the incremental files
url = "https://www.nseindia.com/api/corporates-pit?index=equities&csv=true"
driver.get(url)

time.sleep(50)
all_filenames = [i for i in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension))]

#Dowloading the data
dfs = []
for filename in all_filenames:
        f = pd.read_csv(filename)
        if f.empty == False :
        	f.columns = f.columns.str.strip()
        	dfs.append(f)

#extracting the columns
data = pd.concat(dfs, ignore_index=True)
data.columns=data.columns.str.strip()
data = data[['SYMBOL', 'COMPANY',  'NAME OF THE ACQUIRER/DISPOSER', 'CATEGORY OF PERSON', '% SHAREHOLDING (PRIOR)', 'NO. OF SECURITIES (ACQUIRED/DISPLOSED)', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED)', 'ACQUISITION/DISPOSAL TRANSACTION TYPE', 'TYPE OF SECURITY (POST)', 'NO. OF SECURITY (POST)',  'MODE OF ACQUISITION', 'BROADCASTE DATE AND TIME']]
data = data.sort_values(["SYMBOL"], ascending=True)

#for handling Nil values as 0 
temp = []
for item in data['NO. OF SECURITY (POST)']:
	if (str(item)) == 'Nil':
		item_v = str(0)
	else:
		item_v = item
	temp.append(item_v)
data.loc[:, 'NO. OF SECURITY (POST)'] = temp 
data.drop_duplicates()

data = data.sort_values(["SYMBOL"],ascending=True)
data.reset_index( inplace=True)
data.drop('index', axis=1, inplace=True)

#print(data.columns)

#SQL details
conn = pyodbc.connect('Driver={SQL Server};'
               'Server=DESKTOP-OCIQVL0;'
               'Database=InsiderDatabase;'
               'Trusted_Connection=yes;')
cursor = conn.cursor()

#Insert DataFrame to Table
for row in data.itertuples(index=False):
         print(row[11])
         cursor.execute('''INSERT INTO InsiderDatabase.dbo.Insider ([SYMBOL],[COMPANY],[NAME OF THE ACQUIRER DISPOSER],[CATEGORY OF PERSON],[% SHAREHOLDING (PRIOR)],[NO  OF SECURITIES (ACQUIRED DISPLOSED)],[VALUE OF SECURITY (ACQUIRED DISPLOSED)],[ACQUISITION DISPOSAL TRANSACTION TYPE],[TYPE OF SECURITY (POST)],[NO  OF SECURITY (POST)],[MODE OF ACQUISITION],[BROADCASTE DATE AND TIME])
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
               ''',
         row[0], 
         row[1],
         row[2],
         row[3],
         row[4],
         row[5], 
         row[6],
         row[7],
         row[8],
         row[9],
         row[10],
         row[11]
         )

conn.commit()



