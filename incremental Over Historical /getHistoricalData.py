#https://www.nseindia.com/api/corporates-pit?index=equities&from_date=08-06-2019&to_date=08-06-2020&symbol=SBIN&csv=true

#File to be run once to extract historical data and saving it as a csv


#importing all libraries
import pandas as pd
from selenium import webdriver
import glob
import os
import time
from csv import reader



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


#export to csv -- for the sake of use in the incremental data
data.to_csv("Insider_historical.csv", index = False)




