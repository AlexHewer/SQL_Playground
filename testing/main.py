'''This is for testing databases'''

import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};' # pylint: disable=c-extension-no-member
                      'Server=IBM-PF3TSS1L\SQLEXPRESS;' # pylint: disable=anomalous-backslash-in-string
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('USE CarDealership')
cursor.execute('SELECT Name FROM Models')

for i in cursor:
    print(i[0])

df = pd.read_sql_query('SELECT * FROM Models', conn)

print(df)
