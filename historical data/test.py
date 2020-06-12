import pandas as pd

d1 = pd.read_csv('final_data.csv')
print(d1.info())

d2 = pd.read_csv('final_data_Jun12.csv')
d2['NO. OF SECURITIES (ACQUIRED/DISPLOSED)'] = d2['NO. OF SECURITIES (ACQUIRED/DISPLOSED)'].astype(str).astype(float)
d2['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'] = d2['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'].astype(str).astype(float)
print(d2.info())