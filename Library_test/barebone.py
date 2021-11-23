"Libraries are used for :"
"""html5lib is used to manage the html section of the page"""
import html5lib
from bs4 import BeautifulSoup
"""BeautifulSoup is handling the web scraping portions of the code"""
import requests
"""requests handle the url requests potions"""

url = "https://en.wikipedia.org/wiki/Rose"
"""The url of the page,
    later this would be generated using some automation scripts"""

r = requests.get(url)
#?
"""Change the comment when you know what is the use of that reuests.get()"""

soup = BeautifulSoup(r.text, 'html.parser')
# this parses a document.
#syntax: <var> = BeautifulSoup(<string/open file handle>)
""" Open File Handle is a temporary file name / identifier assigned to an open file that's currently being utilized by an OS 
