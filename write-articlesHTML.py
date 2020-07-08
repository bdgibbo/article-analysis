#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:54:52 2020

@author: bengibbons
"""

# write-html.py
import webbrowser

f = open('ArticleAnalysis.html','w')

article_sample = "Article: New York Times. Ben is Awesome"

message = """<html>

<h1>Article Sentiment Analysis</h1>
<body style="background-color:lightcyan;">

<h2>Instructions</h2>
<p>Instructions for the raters will appear here. It is important that this
is clear and concise. I wonder if I spelled concise correctly...It could be
conscice. No, that doesn't look right. Concise it is.</p>

<h2>Article Sample</h2>
<p>Somehow, the article sample needs to go here. The sample will be drawn from
an SQL-query and can be anything from a sentence to the entire article. Thus,
this will need to be generalized to take a parameter.<br>
Update: as long as the query can be assigned to my variable (currently
called article_sample), we might be in ok shape...</p>
"""
f.write(message)

# article sample will contain url and sample -- need to grab article sample
f.write(article_sample)

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