import pandas as pd
from selenium import webdriver

#driver = webdriver.Chrome(ChromeDriverManager().install())




chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/InsiderTrading'}
chrome_options.add_experimental_option('prefs', prefs)






chrome_path = "/Users/abhishek/Desktop/William-O-Neal-Data-Analytics/chromedriver"

driver = webdriver.Chrome(chrome_path, options=chrome_options)

url = "https://www.nseindia.com/api/corporates-pit?index=equities&csv=true"
driver.get(url)





#driver.delete_all_cookies()
#driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/section/div/div/div/div/div[1]/d#v/div[4]/div[1]/div").click()

