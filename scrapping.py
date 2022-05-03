
import pandas as pd
import csv
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import copy 

# Python program to print all heading tags
 
# scraping 
url = 'https://api.opendata.onisep.fr/tmp/23/ec/26ca3be7fe8f9b69b93273ef3b43/ideo-formations_initiales_en_france.xml'
request = requests.get(url)
 
Soup = BeautifulSoup(request.text, 'lxml')
 
# creating a list of all common heading tags
heading_tags = ['code_cnis', 'sigle_type_formation', 'libelle_type_formation', 'libelle_formation_principal', 'sigle_formation', 'duree', 'code_rncp', 'niveau_rncp', 'libelle_niveau_rncp', 'tutelle', 'lien_site_onisepfr', 'domainesous-domaine']

forma_buffer = {}
liste_formas = []
for i, tags in enumerate(Soup.find_all(heading_tags)):
    if (i % len(heading_tags) != 0):
        forma_buffer[tags.name] = tags.text
    else:
        liste_formas.append(copy.deepcopy(forma_buffer))

df = pd.DataFrame.from_dict(liste_formas).dropna()
df