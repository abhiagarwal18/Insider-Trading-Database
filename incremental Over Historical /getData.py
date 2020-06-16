import pandas as pd
from selenium import webdriver
import glob
import os
import time
import pyodbc

#driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\\Users\\hritw\\Desktop\\William O Neil\\Insider-Trading-Database-master\\Insider-Trading-Database-master'}
chrome_options.add_experimental_option('prefs', prefs)
chrome_path = "C:\\Users\\hritw\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(chrome_path, options=chrome_options)


extension = 'csv'
path = "C:\\Users\\hritw\\Desktop\\William O Neil\\Insider-Trading-Database-master\\Insider-Trading-Database-master"


for filename in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension)):
   os.remove(filename) 


url = "https://www.nseindia.com/api/corporates-pit?index=equities&csv=true"
driver.get(url)

time.sleep(5)
all_filenames = [i for i in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension))]
original_file = "C:\\Users\\hritw\\Desktop\\William O Neil\\Insider-Trading-Database-master\\Insider-Trading-Database-master\\Insider_historical.csv"


#list_columns = ['SYMBOL',"COMPANY", "NAME OF THE ACQUIRER/DISPOSER", "CATEGORY OF PERSON","TYPE OF SECURITY (PRIOR)","NO. OF SECURITY (PRIOR)", "% SHAREHOLDING (PRIOR)","NO. OF SECURITIES (ACQUIRED/DISPLOSED)","VALUE OF SECURITY (ACQUIRED/DISPLOSED)","ACQUISITION/DISPOSAL TRANSACTION TYPE","TYPE OF SECURITY (POST)","NO. OF SECURITY (POST)","% POST","DATE OF ALLOTMENT/ACQUISITION FROM","DATE OF ALLOTMENT/ACQUISITION TO","DATE OF INITMATION TO COMPANY","MODE OF ACQUISITION","EXCHANGE"]
#combine all files in the list

dfs = []
for filename in all_filenames:
        f = pd.read_csv(filename)
        if f.empty == False :
        	f.columns = f.columns.str.strip()
        	dfs.append()

o = pd.read_csv(original_file)
o.columns = o.columns.str.strip()
dfs.append(o)
        
#concat
data = pd.concat(dfs, ignore_index=True)
data.columns=data.columns.str.strip()
data = data.sort_values(["SYMBOL"], ascending=True)


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


#export to csv
#combined_csv.to_csv("IncrementalPlusHistory.csv", index = False)

conn = pyodbc.connect('Driver={SQL Server};'
               'Server=DESKTOP-OCIQVL0;'
               'Database=InsiderDatabase;'
               'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute("""CREATE TABLE [dbo].[IH] (
         [Index] int,
[SYMBOL] varchar(50),
[COMPANY] varchar(150),
[NAME OF THE ACQUIRER DISPOSER] varchar(150),
[CATEGORY OF PERSON] varchar(150),
[% SHAREHOLDING (PRIOR)] float,
[NO  OF SECURITIES (ACQUIRED DISPLOSED)] bigint,
[VALUE OF SECURITY (ACQUIRED DISPLOSED)] float,
[ACQUISITION DISPOSAL TRANSACTION TYPE] varchar(50),
[TYPE OF SECURITY (POST)] varchar(50),
[NO  OF SECURITY (POST)] bigint,
[MODE OF ACQUISITION] varchar(50),
[BROADCASTE DATE AND TIME] datetime
)""")


# Insert DataFrame to Table
for row in data.itertuples():
         print(row[11])
         cursor.execute('''INSERT INTO InsiderDatabase.dbo.IH ([SYMBOL],[COMPANY],[NAME OF THE ACQUIRER DISPOSER],[CATEGORY OF PERSON],[% SHAREHOLDING (PRIOR)],[NO  OF SECURITIES (ACQUIRED DISPLOSED)],[VALUE OF SECURITY (ACQUIRED DISPLOSED)],[ACQUISITION DISPOSAL TRANSACTION TYPE],[TYPE OF SECURITY (POST)],[NO  OF SECURITY (POST)],[MODE OF ACQUISITION],[BROADCASTE DATE AND TIME])
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

#cursor.fast_executemany = True
#for row_count in range(0, df.shape[0]):
#   chunk = df.iloc[row_count:row_count + 1,:].values.tolist()
#   tuple_of_tuples = tuple(tuple(x) for x in chunk)
#   cursor.executemany("INSERT INTO InsiderDatabase.dbo.historical" + " ([SYMBOL],[COMPANY],[NAME OF THE ACQUIRER DISPOSER],[CATEGORY OF PERSON],[% SHAREHOLDING (PRIOR)],[NO  OF SECURITIES (ACQUIRED DISPLOSED)],[VALUE OF SECURITY (ACQUIRED DISPLOSED)],[ACQUISITION DISPOSAL TRANSACTION TYPE],[TYPE OF SECURITY (POST)],[NO  OF SECURITY (POST)],[MODE OF ACQUISITION],[BROADCASTE DATE AND TIME]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",tuple_of_tuples)


conn.commit()

