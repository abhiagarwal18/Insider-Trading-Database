import pandas as pd
from selenium import webdriver
import glob
import os
import time
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
original_file = "C:\\Users\\hritw\\Desktop\\William O Neil\\Insider-Trading-Database-master\\Insider-Trading-Database-master\\Insider.csv"


#list_columns = ['SYMBOL',"COMPANY", "NAME OF THE ACQUIRER/DISPOSER", "CATEGORY OF PERSON","TYPE OF SECURITY (PRIOR)","NO. OF SECURITY (PRIOR)", "% SHAREHOLDING (PRIOR)","NO. OF SECURITIES (ACQUIRED/DISPLOSED)","VALUE OF SECURITY (ACQUIRED/DISPLOSED)","ACQUISITION/DISPOSAL TRANSACTION TYPE","TYPE OF SECURITY (POST)","NO. OF SECURITY (POST)","% POST","DATE OF ALLOTMENT/ACQUISITION FROM","DATE OF ALLOTMENT/ACQUISITION TO","DATE OF INITMATION TO COMPANY","MODE OF ACQUISITION","EXCHANGE"]
#combine all files in the list

dfs = []
for filename in all_filenames:
        f = pd.read_csv(filename)
        if f.empty == False :
        	f.columns = f.columns.str.strip()
        	dfs.append(f.iloc[:,0:-10])

o = pd.read_csv(original_file)
o.columns = o.columns.str.strip()
dfs.append(o)
        
#concat
combined_csv = pd.concat(dfs, ignore_index=True)
combined_csv.columns=combined_csv.columns.str.strip()
combined_csv = combined_csv.sort_values(["SYMBOL"], ascending=True)

#export to csv
combined_csv.to_csv("IncrementalPlusHistory.csv", index = False)



