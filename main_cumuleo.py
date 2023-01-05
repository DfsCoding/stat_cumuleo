from pprint import pprint

import pandas as pd
import requests
import string

from bs4 import BeautifulSoup

import constants




def get_url_mandataires(soupehtml):
    url_mandataires = []
    nom_mandataires = []
   
    for nom in soupehtml.findAll("li", attrs={"class": "listingli"}):
        url_mandat = nom.a["href"]
        nom_mandat = nom.b.text.strip()
        url_mandataires.append(url_mandat)
        nom_mandataires.append(nom_mandat)
     
    
    return (nom_mandataires , url_mandataires)


def get_html(url):
    alphabet = string.ascii_lowercase
    nom_mandataires_lst = []
    url_mandataires_lst = []
    for lettre in alphabet:
        web_page = requests.get(url + lettre)
        soup = BeautifulSoup(web_page.content, 'html5lib')
        nom_mandataires,url_mandataires = get_url_mandataires(soup)
        nom_mandataires_lst.extend(nom_mandataires)
        url_mandataires_lst.extend(url_mandataires)
    
    print(nom_mandataires_lst.__len__())
    return zip (nom_mandataires_lst , url_mandataires_lst)
    

# Récupèrer tuples (mandataire, url vers détails)
mandataires_url_details_lst = get_html(constants.representative_url_list_base)
#pprint (list (mandataires_url_details_lst))

# Récupérer liste des tableaux
for mandataire,url_details in list(mandataires_url_details_lst):
    print(mandataire , url_details)
    html_f = requests.get(url_details)
    html_soup = BeautifulSoup(html_f.content,'html5lib')
    tables_soup = html_soup.find_all("table", attrs={'class':'listemandats'})
    print(tables_soup)
    rep = input("Continue ?")
    if rep.capitalize=='N':
        break