#https://www.nseindia.com/api/corporates-pit?index=equities&from_date=08-06-2019&to_date=08-06-2020&symbol=SBIN&csv=true

#File to be run once to extract historical data and saving it as a csv


#importing all libraries
import pandas as pd
from selenium import webdriver
import glob
import os
import time
from csv import reader
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


'''

#for chromedriver
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'PATH1'}
chrome_options.add_experimental_option('prefs', prefs)


chrome_path = "PATH2"
driver = webdriver.Chrome(chrome_path, options=chrome_options)

#cleaning existing files
extension = 'csv'
path = "PATH3"

for filename in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension)):
   os.remove(filename)

company_list = (os.path.join(path,"EQUITY_L.{}").format(extension))




#downloading historical data
with open(company_list, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    header = next(csv_reader)
    # Check file as empty
    if header != None:
    for row in csv_reader:
    if any(row):
    symbol = row[0]
    print(row[0])
    url = "https://www.nseindia.com/api/corporates-pit?index=equities&from_date=08-06-2019&to_date=08-06-2020&symbol="+symbol+"&csv=true"
    driver.get(url)
    else:
    break

time.sleep(50)
all_filenames = [i for i in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension))]

#concatenate for all the companies
dfs = []
for filename in all_filenames:
        f = pd.read_csv(filename)
        if f.empty == False :
        f.columns = f.columns.str.strip()
        dfs.append(f)

data = pd.concat(dfs, ignore_index=True)

#extracting the desired columns
data.columns=data.columns.str.strip()
data = data.sort_values(["SYMBOL"], ascending=True)
data = data[['SYMBOL', 'COMPANY',  'NAME OF THE ACQUIRER/DISPOSER', 'CATEGORY OF PERSON', '% SHAREHOLDING (PRIOR)', 'NO. OF SECURITIES (ACQUIRED/DISPLOSED)', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED)', 'ACQUISITION/DISPOSAL TRANSACTION TYPE', 'TYPE OF SECURITY (POST)', 'NO. OF SECURITY (POST)',  'MODE OF ACQUISITION', 'BROADCASTE DATE AND TIME']]

data.reset_index( inplace=True)
data.index.name = 'SINo'
data.drop('index', axis=1, inplace=True)
   
#export to csv -- for the sake of use in the incremental data
data.to_csv("Insider_historical.csv")


#CLEANING BEFORE PASSING TO SQL

temp3 = []
temp2 = []
temp1 = []
temp = []
for item in data['COMPANY']:
    if item != item:
        item_v = '-'
    else:
        item_v = item
    temp3.append(item_v)
data.loc[:, 'COMPANY'] = temp3

for item in data['VALUE OF SECURITY (ACQUIRED/DISPLOSED)']:
    if item != item:
        item_v = 0
    elif (str(item)) == '-':
        item_v=0
    else:
        item_v = item
    temp2.append(item_v)
data.loc[:, 'VALUE OF SECURITY (ACQUIRED/DISPLOSED)'] = temp2

for item in data['NO. OF SECURITIES (ACQUIRED/DISPLOSED)']:
    if item != item:
        item_v = 0
    elif (str(item)) == '-':
        item_v=0
    else:
        item_v = item
    temp1.append(item_v)
data.loc[:, 'NO. OF SECURITIES (ACQUIRED/DISPLOSED)'] = temp1

for item in data['NO. OF SECURITY (POST)']:
    if (str(item)) == 'Nil':
        item_v = 0
    elif (str(item)) == '-':
        item_v=0
    else:
        item_v = item
    temp.append(item_v)
data.loc[:, 'NO. OF SECURITY (POST)'] = temp
data.drop_duplicates()



data = data.sort_values(["SYMBOL"],ascending=True)
data.reset_index( inplace=True)
data.drop('index', axis=1, inplace=True)

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-OCIQVL0;'
                        'Database=InsiderDatabase;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()

        # Create Table

        # Insert DataFrame to Table
for row in data.itertuples(index = False):
    print(row[:])
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