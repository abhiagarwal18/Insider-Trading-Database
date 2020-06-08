from time import sleep
from selenium import webdriver
from dataProcessor import preprocess
import pandas as pd
import os
import shutil
import time



#DEFINE ALL THE PATHS 

download_path = '/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/InsiderTrading'
chromedriver_path = "/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/chromedriver"

#DOWNLOADING THE DATA FROM THE NSE WEBSITE 
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
chrome_options.add_experimental_option('prefs', prefs)
chrome_path = chromedriver_path
driver = webdriver.Chrome(chrome_path, options=chrome_options)
url = "https://www.nseindia.com/api/corporates-pit?index=equities&csv=true"
driver.get(url)

#SLEEPING TO WAIT FOR THE DOWNLOAD TO COMPLETE
sleep(10)

preprocess(download_path)