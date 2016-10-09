import urllib
import re
from bs4 import BeautifulSoup
import csv

depart ="https://fr.wikipedia.org/wiki/Liste_des_monuments_historiques_de_Strasbourg"
url = urllib.urlopen(depart).read() # on demande à urllib d'ouvrir notre url...
soupe = BeautifulSoup(url) # ... et on la transforme en élément BS

tableau = soupe.find("table", {"class":"wikitable sortable"})  # on considère le premier tableau de classe "wikitable sortable"
lignes = tableau.findAll("tr")  # à l'intérieur duquel on prend toutes les lignes
ficsv = open('monuments_histo_strabourg.csv','w+')

try:
	majcsv = csv.writer(ficsv)
	majcsv.writerow(('Monument','Adresse','Longitude','Latitude','Source')) # les noms de colonne évidemment avant la boucle
	for ligne in lignes:
		monuments = ligne.findAll("td") # on fait nos premières sélections
		longitude = ligne.find("data", {"class":"p-longitude"})
		latitude = ligne.find("data", {"class":"p-latitude"})
		source = ligne.findAll("a", {"href":re.compile("^http://www.culture.gouv")}) 
		if monuments and longitude and latitude and source: # et on balance si elles existent
			monument = monuments[0].get("data-sort-value").encode('utf-8') # obligé d'encoder en UTF-8, sinon ça finit par planter
			adresse = monuments[1].get_text().encode('utf-8')
			longitude_valeur = longitude.get('value')
			latitude_valeur = latitude.get('value')
			lien = source[0].get('href')
			majcsv.writerow((monument, adresse, longitude_valeur, latitude_valeur, lien))
finally:
	ficsv.close()
