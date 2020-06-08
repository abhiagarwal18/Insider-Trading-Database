# Insider-Trading-Database
Python script to extract real-time csv from the NSE official website 

1.) At first, in order to download the historical data, first remove all the csv files( starting from - "CF-Insider-Trading-equities-* though it is uneccessary).

2.) After that, it iterates over the EQUITY_L file and extracts the symbol name and downloads data for all those companies.

3.)If the file is empty, ignore it. Otherwise, add it to the list and finally concat them using pandas(sorting based on SYMBOL as of now).

4.) File Insider.csv contains the historical data.
