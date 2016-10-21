# Scrapers monuments historiques

Ces deux scripts codés en Python permettent d'ordonner dans des CSV **les principales informations de pages Wikipedia consacrées aux monuments historiques** (Strasbourg et principales villes du Grand-Est).

L'objectif est grosso modo de se retrouver avec un fichier qui est traduisible par QGis :

![CSV_QGis](http://raphi.m0le.net/blog/images/monuments_ge.png)

Ces scripts utilisent les modules urllib, BeautifulSoup, re et csv. A noter que ces scripts ont été codés sous une distribution Debian, donc pas avec la dernière version de Python.

Les recettes sont détaillées [sur ce blog](http://raphi.m0le.net/blog/sraper-wikipedia-python.html) !

EDIT : j'ai ajouté une version qui tourne sur Python 3. Pour gérer plus efficacement l'encodage, j'ai préféré requests à urllib !
