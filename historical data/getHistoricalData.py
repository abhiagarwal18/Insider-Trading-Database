#https://www.nseindia.com/api/corporates-pit?index=equities&from_date=08-06-2019&to_date=08-06-2020&symbol=SBIN&csv=true
import pandas as pd
from selenium import webdriver
import glob
import os
import time
from csv import reader

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

company_list = (os.path.join(path,"EQUITY_L.{}").format(extension))


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

#chdir(path)
time.sleep(500)
all_filenames = [i for i in glob.glob(os.path.join(path,"CF-Insider-Trading-equities-*.{}").format(extension))]

#original_file = "C:\\Users\\hritw\\Desktop\\William O Neil\\Insider-Trading-Database-master\\Insider-Trading-Database-master\\Historical.csv"


#list_columns = ['SYMBOL',"COMPANY", "NAME OF THE ACQUIRER/DISPOSER", "CATEGORY OF PERSON","TYPE OF SECURITY (PRIOR)","NO. OF SECURITY (PRIOR)", "% SHAREHOLDING (PRIOR)","NO. OF SECURITIES (ACQUIRED/DISPLOSED)","VALUE OF SECURITY (ACQUIRED/DISPLOSED)","ACQUISITION/DISPOSAL TRANSACTION TYPE","TYPE OF SECURITY (POST)","NO. OF SECURITY (POST)","% POST","DATE OF ALLOTMENT/ACQUISITION FROM","DATE OF ALLOTMENT/ACQUISITION TO","DATE OF INITMATION TO COMPANY","MODE OF ACQUISITION","EXCHANGE"]
#combine all files in the list
dfs = []
for filename in all_filenames:
        f = pd.read_csv(filename)
        if f.empty == False :
        	f.columns = f.columns.str.strip()
        	dfs.append()

combined_csv = pd.concat(dfs, ignore_index=True)

combined_csv.columns=combined_csv.columns.str.strip()
combined_csv = combined_csv.sort_values(["SYMBOL"], ascending=True)


combined_csv = combined_csv[['SYMBOL', 'COMPANY',  'NAME OF THE ACQUIRER/DISPOSER', 'CATEGORY OF PERSON', '% SHAREHOLDING (PRIOR)', 'NO. OF SECURITIES (ACQUIRED/DISPLOSED)', 'VALUE OF SECURITY (ACQUIRED/DISPLOSED)', 'ACQUISITION/DISPOSAL TRANSACTION TYPE', 'TYPE OF SECURITY (POST)', 'NO. OF SECURITY (POST)',  'MODE OF ACQUISITION', 'BROADCASTE DATE AND TIME']]
combined_csv.to_csv('final_historical_data.csv', index = False)    






