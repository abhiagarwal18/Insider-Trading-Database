from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
startTime = datetime.now()

import pandas as pd


chrome_path = "/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/chromedriver"
chrome_options = Options()  
chrome_options.add_argument("headless") 
driver = webdriver.Chrome(chrome_path,options=chrome_options,keep_alive=False)
driver = webdriver.Chrome(chrome_path)
url = "https://www.nseindia.com/companies-listing/corporate-filings-insider-trading?desk=yes"
driver.get(url)


tickerlist=[]
disposerlist=[]
numberOfSecuritieslist=[]
acquisitionDisposallist=[]
broadcastdatetimelist = []

for i in range(1,255):


    tickerpath = f"""//*[@id="CFinsidertradingTable"]/tbody/tr[{i}]/td[1]"""
    ticker = driver.find_element_by_xpath(tickerpath)
    tickerlist.append(ticker.text)

    disposerpath = f"""//*[@id="CFinsidertradingTable"]/tbody/tr[{i}]/td[4]"""
    disposer = driver.find_element_by_xpath(disposerpath)
    disposerlist.append(disposer.text)

    numberOfSecuritiespath = f"""//*[@id="CFinsidertradingTable"]/tbody/tr[{i}]/td[6]"""
    numberOfSecuritites = driver.find_element_by_xpath(numberOfSecuritiespath)
    numberOfSecuritieslist.append(numberOfSecuritites.text)

    acquisitionDisposalpath = f"""//*[@id="CFinsidertradingTable"]/tbody/tr[{i}]/td[7]"""
    acquisitionDisposal = driver.find_element_by_xpath(acquisitionDisposalpath)
    acquisitionDisposallist.append(acquisitionDisposal.text)

    broadcastdatetimepath = f"""//*[@id="CFinsidertradingTable"]/tbody/tr[{i}]/td[8]"""
    broadcastdatetime = driver.find_element_by_xpath(broadcastdatetimepath)
    broadcastdatetimelist.append(broadcastdatetime.text)


allinfo = list(zip(tickerlist, disposerlist, numberOfSecuritieslist, acquisitionDisposallist, broadcastdatetimelist))

df = pd.DataFrame(
        allinfo,
        columns=["Ticker", "Disposer", "Number of Securities", "Acquisition/Disposal", "Broadcasted Date/Time"])

df.to_csv('Insider.csv',index=False)

print(f"""Execution Time: {datetime.now() - startTime}""")





