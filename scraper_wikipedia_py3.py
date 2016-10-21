#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
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
		url = requests.get(url_ville) # et on ouvre chacune d'entre elles
		print("Lien : "+url_ville)
		soupe = BeautifulSoup(url.text)
		tableau = soupe.find("table", {"class":"wikitable sortable"}) # on chope le premier tableau de classe "wikitable sortable"
		lignes = tableau.findAll("tr") # puis toutes ses lignes
		for ligne in lignes:
			monuments = ligne.findAll("td") # on fait les premières sélections
			longitude = ligne.find("data", {"class":"p-longitude"})
			latitude = ligne.find("data", {"class":"p-latitude"})
			source = ligne.findAll("a", {"href":re.compile("^http://www.culture.gouv")}) 
			if monuments and longitude and latitude and source:
				monument = monuments[0].get("data-sort-value") # si les sélections existent, on balance
				adresse = monuments[1].get_text()
				longitude_valeur = longitude.get('value')
				latitude_valeur = latitude.get('value')
				lien = source[0].get('href')
				print(monument, adresse, longitude_valeur, latitude_valeur, source)
				majcsv.writerow((monument, adresse, longitude_valeur, latitude_valeur, lien))
finally:
	ficsv.close()
