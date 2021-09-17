#!/usr/bin/python3
#lucky.py - open several google search results

import requests, sys, webbrowser, bs4

start = input("Please the page where to start: ")
stop = input("Please the page where to stop: ")
link = input("Please the argument link \n\n:")

print ("Donwloading the link from: " + str(link)) 
print ("Starting from page: " + str(start) + " to " + str(stop))
print ('Starting...')

#number of the page of the link, 
# for example ?page=1, ?page=2
for i in range(int(start),int(stop)):																		
	print ('\nWORKING ON PAGE: '+str(i))
	res = requests.get(str(link) + '?page=' + str(i))	#CAMBIA QUI per l'argomento
	res.raise_for_status()

	# retrive links
	soup = bs4.BeautifulSoup(res.text, "lxml")

	# find link for each result
    # '.name ' for <li class="name">   
    # 'a'      for <a href="link_to_open(relative_path)">...</a>
	linkElems = soup.select('. a')

	numOpen = min(40, len(linkElems))      #numbers of link per page
	for i in range (numOpen):
		print('\ndownloading link: '+ linkElems[i].get('href'))
		res = requests.get('http://www.battlecraft.it' + linkElems[i].get('href'))
        
        #failure control
		if (res.status_code != requests.codes.ok):
			print("failed saving " + linkElems[i].get('href'))



		name = linkElems[i].get('href')
		name = name.replace('/', '-')
		name += '.html' 

        #save the page in a .html file with the name of the relative path
		playFile = open(name,'wb')
		for chunk in res.iter_content(100000):
			playFile.write(chunk)
		playFile.close()
