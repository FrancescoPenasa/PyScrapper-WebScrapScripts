#!/usr/bin/python3
#lucky.py - open several google search results

import requests, sys, webbrowser, bs4
print ('Im working')
for i in range(1,4):																		#CAMBIA QUI, esempio: (1,54) per le pagine da 1 a 53 compresa
	print ('\nWORKING ON PAGE: '+str(i))
	res = requests.get('http://www.battlecraft.it/starcraft/notizie?page='+str(i))	#CAMBIA QUI per l'argomento
	res.raise_for_status()


	# retrive top search result link
	soup = bs4.BeautifulSoup(res.text, "lxml")

	# open a broswer tab for each result
	linkElems = soup.select('. a')

	numOpen = min(40, len(linkElems))      #CAMBIA QUI IL NUMERO DI LINKS DA SCARICARE (consiglio di lasciarlo a 40, altrimenti poi è un casino)
	for i in range (numOpen):
		print('\ndownloading link: '+ linkElems[i].get('href'))
		res = requests.get('http://www.battlecraft.it' + linkElems[i].get('href'))
		if (res.status_code != requests.codes.ok):
			print("failed saving " + linkElems[i].get('href'))

		name = linkElems[i].get('href')
		name = name.replace('/', '-')
		s = '.html'
		name = name + s 
		
		playFile = open(name,'wb')
		
		for chunk in res.iter_content(100000):
			playFile.write(chunk)
		
		playFile.close()
