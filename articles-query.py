# Import required packages

import pyodbc
import random
import re

# Connect to database
conn = pyodbc.connect('''Driver={ODBC Driver 17 for SQL Server};
                      Server=tcp:51.79.87.60;
                      PORT=1433;
                      Database=master;
                      UID=SA;
                      PwD=HeZAdgD55M5k;''')

cursor = conn.cursor()

# SQL query to randomly select one url and content from random source
randsource = random.randrange(0, 3, 1)

if randsource == 0:
    cursor.execute('SELECT TOP 1 url, content FROM [master].[dbo].[CLEAN_FOX] ORDER BY NEWID()')
elif randsource == 1:
    cursor.execute('SELECT TOP 1 url, content FROM [master].[dbo].[RAW_NYT] ORDER BY NEWID()')
elif randsource == 2:
    cursor.execute('SELECT TOP 1 url, content FROM [master].[dbo].[RAW_BBC] ORDER BY NEWID()')
else:
    pass

#gets all data from SQL query (row[0] = url. row[1] = content
records = cursor.fetchall()

#defines variables form records object
for row in records:
        url = row[0]
        content = row[1]

#splits content list into indvidual sentences
contentlist = content.split('. ')
l = re.compile("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s").split(content)

#defines the total rows from which to randomly select
rowtotal = len(l)

#randomly selects from list of sentences (-3 is a hacky way used to avoid end of page BS)
randline = random.randrange(1, (rowtotal) - 3)


#prints the url
print(url)

#prints the sentence
print(l[randline])