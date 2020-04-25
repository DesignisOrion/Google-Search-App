# This project is what they call it funscript because it's a project that's pure fun
# Project will allow us to create a google searcher in 10 lines of code.
# This program will allow you to search via google anything and 5 tabs will popup.

import requests
import sys
import webbrowser
import bs4


res = requests.get('htttps://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElements = soup.select('.r a')
linkToOpen = min(5, len(linkElements))

for i in range(linkToOpen):
    webbrowser.open('https://google.com' + linkElements[i].get('href'))
