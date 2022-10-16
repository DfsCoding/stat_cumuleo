from pprint import pprint

import requests
import string

from bs4 import BeautifulSoup

import constants


# def get_mandataires(soupehtml):
#    mandataires = []
#    for nom in soupehtml.findAll("span" ,  attrs = { "class": "listingnom"}):
#            mandataires.append(nom.text.strip())

#    return mandataires

def get_url_mandataires(soupehtml):
    url_mandataires = []
    nom_mandataires = []
    mandatataires_lst = {}
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
    


#pprint (list (get_html(constants.url_to_2020)))
get_html(constants.url_to_2020)