#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:54:52 2020

@author: bengibbons
"""

import webbrowser
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
#print(url)

#prints the sentence
#print(l[randline])


# write-html
f = open('ArticleAnalysis.html','w')

article_sample = randline

message = """<html>

<h1>Article Sentiment Analysis</h1>
<body style="background-color:lightcyan;">

<h2>Instructions</h2>
<p>Instructions for the raters will appear here.</p>

<h2>Article Sample</h2>
<p>The url and article sample appear below:</p>
"""
f.write(message)

f.write(url)
f.write("<html><p></p></html>")
f.write(l[randline])

message = """<html>
<h2>Rating</h2>
<p>Please rate the above text using the mechanism below.</p>
<form>
    <input type="radio" id="happy" name="sentiment" value="happy">
    <label for="happy">Happy</label><br>
    <input type="radio" id="neutral" name="sentiment" value="neutral">
    <label for="neutral">Neutral</label><br>
    <input type="radio" id="sad" name="sentiment" value="sad">
    <label for="sad">Sad</label><br>
    <input type="submit" value="Submit">
</form>


<h2>Congratulations! You're done! Thank you for helping us out.</h2>

</body>
</html>"""

f.write(message)
f.close()


#Change path to reflect file location
filename = 'file:///Users/bengibbons/Desktop/' + 'ArticleAnalysis.html'
webbrowser.open_new_tab(filename)
