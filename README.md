# Insider-Trading-Database
Python script to extract real-time csv from the NSE official website 

## Authors
* Abhishek Agarwal 
* Hritwik Goklaney


# Incremental Database

## Requirements ##

A virtual environment with the following packages installed :

* pandas
* os
* selenium
* shutil
* glob

## Usage ##

* Enter the path to the directory (the same one having the python codes) as the download_path
* Download and unpack the chromedriver in the same directory and enter its path in the corresponding variable
* run the "run.py" file using the command

_python3 run.py_

* the final csv file will be saved as "final_data.csv"
* The same script can be run on a daily basis to update the latest insider trading data

# Historical Database