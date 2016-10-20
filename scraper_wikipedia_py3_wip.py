#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import re
from bs4 import BeautifulSoup
import csv

depart ="https://fr.wikipedia.org/wiki/Liste_des_monuments_historiques_d"
villes = ["e_Reims", "e_Chaumont", "e_Charleville-Mézières", "e_Toul", "e_Pont-à-Mousson", "e_Haguenau", "e_Châlons-en-Champagne", "e_Troyes", "e_Verdun", "e_Bar-le-Duc", "'Épinal", "e_Nancy", "e_Metz", "e_Colmar", "e_Sélestat", "e_Mulhouse", "e_Strasbourg"]
print(villes)
ficsv = open('monuments_histo_ge.csv','w+')

try:
	majcsv = csv.writer(ficsv)
	majcsv.writerow(('Monument','Adresse','Longitude','Latitude','Source'))
	for ville in villes:
		url_ville = depart+ville # une simple addition de chaînes de cara' nous donne nos URL complètes
		url = urllib.request.urlopen(url_ville).read() # et on ouvre chacune d'entre elles
		print("Lien : "+url_ville)
		soupe = BeautifulSoup(url)
		tableau = soupe.find("table", {"class":"wikitable sortable"}) # on chope le premier tableau de classe "wikitable sortable"
		lignes = tableau.findAll("tr") # puis toutes ses lignes
		for ligne in lignes:
			monuments = ligne.findAll("td") # on fait les premières sélections
			longitude = ligne.find("data", {"class":"p-longitude"})
			latitude = ligne.find("data", {"class":"p-latitude"})
			source = ligne.findAll("a", {"href":re.compile("^http://www.culture.gouv")}) 
			if monuments and longitude and latitude and source:
				monument = monuments[0].get("data-sort-value") # si les sélections existent, on balance
				if monument: # là j'ai dû rajouter un test, ai pas bien compris pourquoi
					monument = monument.encode('utf-8') # on est obligé d'encoder en UTF-8, sinon ça plante
				adresse = monuments[1].get_text().encode('utf-8')
				longitude_valeur = longitude.get('value')
				latitude_valeur = latitude.get('value')
				lien = source[0].get('href')
				print(monument, adresse, longitude_valeur, latitude_valeur, source)
				majcsv.writerow((monument, adresse, longitude_valeur, latitude_valeur, lien))
finally:
	ficsv.close()
