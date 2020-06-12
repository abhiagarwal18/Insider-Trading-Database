import pandas as pd
import pyodbc

# Import CSV
df = pd.read_csv (r'C:\Users\hritw\Desktop\Insider-Trading-Database\historical data\final_data.csv',index_col=False)
print(df.iloc[0])

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OCIQVL0;'
                      'Database=InsiderDatabase;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute("""CREATE TABLE [dbo].[IH] (
[SYMBOL] varchar(50),
[COMPANY] varchar(150),
[NAME OF THE ACQUIRER DISPOSER] varchar(150),
[CATEGORY OF PERSON] varchar(150),
[% SHAREHOLDING (PRIOR)] float,
[NO  OF SECURITIES (ACQUIRED DISPLOSED)] bigint,
[VALUE OF SECURITY (ACQUIRED DISPLOSED)] float,
[ACQUISITION DISPOSAL TRANSACTION TYPE] varchar(50),
[TYPE OF SECURITY (POST)] varchar(50),
[NO  OF SECURITY (POST)] bigint,
[MODE OF ACQUISITION] varchar(50),
[BROADCASTE DATE AND TIME] datetime
)""")


# Insert DataFrame to Table
for row in df.itertuples():
	print(row[11])
	cursor.execute('''INSERT INTO InsiderDatabase.dbo.IH ([SYMBOL],[COMPANY],[NAME OF THE ACQUIRER DISPOSER],[CATEGORY OF PERSON],[% SHAREHOLDING (PRIOR)],[NO  OF SECURITIES (ACQUIRED DISPLOSED)],[VALUE OF SECURITY (ACQUIRED DISPLOSED)],[ACQUISITION DISPOSAL TRANSACTION TYPE],[TYPE OF SECURITY (POST)],[NO  OF SECURITY (POST)],[MODE OF ACQUISITION],[BROADCASTE DATE AND TIME])
		VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
               row[0], 
               row[1],
               row[2],
               row[3],
               row[4],
               row[5], 
               row[6],
               row[7],
               row[8],
               row[9],
               row[10],
               row[11]
              )

#cursor.fast_executemany = True
#for row_count in range(0, df.shape[0]):
#   chunk = df.iloc[row_count:row_count + 1,:].values.tolist()
#   tuple_of_tuples = tuple(tuple(x) for x in chunk)
#   cursor.executemany("INSERT INTO InsiderDatabase.dbo.historical" + " ([SYMBOL],[COMPANY],[NAME OF THE ACQUIRER DISPOSER],[CATEGORY OF PERSON],[% SHAREHOLDING (PRIOR)],[NO  OF SECURITIES (ACQUIRED DISPLOSED)],[VALUE OF SECURITY (ACQUIRED DISPLOSED)],[ACQUISITION DISPOSAL TRANSACTION TYPE],[TYPE OF SECURITY (POST)],[NO  OF SECURITY (POST)],[MODE OF ACQUISITION],[BROADCASTE DATE AND TIME]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",tuple_of_tuples)


conn.commit()