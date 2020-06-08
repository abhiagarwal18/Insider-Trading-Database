# Historical Trading Database

Python script to extract historical trading from the NSE official website 

## Requirements ##
A virtual environment with the following packages installed : 

* pandas
* os
* selenium
* shutil
* glob
* time

## Usage ##

* Enter the path to the directory (the same one having the python codes) for downloading the csv files
* Download and unpack the chromedriver in the same directory and enter its path in the corresponding variable
* run the "getHistoricalData.py" file using the command 

_python3 getHistoricalData.py_ 

* the final csv file will be saved as "final_historical_data.csv" 


