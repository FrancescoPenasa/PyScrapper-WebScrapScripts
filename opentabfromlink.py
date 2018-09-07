#!/usr/bin/python3
#lucky.py - open several google search results

import requests, sys, webbrowser, bs4

print('Googling...') #display text while downloading the GOogle page
res = requests.get('http://www.battlecraft.it/worldofwarcraft/notizie?page='+'1')
res.raise_for_status()

# retrive top search result link
soup = bs4.BeautifulSoup(res.text, "lxml")

# opemn a broswed tab ror each result
linkElems = soup.select('. a')
#for bc.it
#linkElems = soup.select('. a')

numOpen = min(40, len(linkElems))      #open 5 tabs, should be 40
for i in range (numOpen):
    webbrowser.open('http://www.battlecraft.it' + linkElems[i].get('href'))
    if (res.status_code != request.codes.ok):
        print("failed saving " + linkElems[i].get('href'))

