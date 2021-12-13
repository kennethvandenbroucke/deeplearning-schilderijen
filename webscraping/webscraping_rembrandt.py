import requests
from bs4 import BeautifulSoup
import os
from webscraping_functions import save_images, is_url_image

# requests is nodig om de html van de pagina's te verkrijgen
# BeautifulSoup wordt gebruikt om gemakkelijk elementen van de html te kunnen verkrijgen
# os wordt gebruikt om de gewenste opslaglocatie aan te maken als deze nog niet bestaat

URL = 'http://www.rembrandtpainting.net/complete_catalogue/complete_catalogue.htm' # de URL van de beginpagina
baseURL = 'http://www.rembrandtpainting.net/complete_catalogue/' 
# de basis van alle URL's van de complete catalogus, deze is nodig omdat de links van alle paginas
# relatief zijn, hiermee kan de volledige URL gemaakt worden.

img_URLs = [] # een lege lijst aanmaken waar alle URLs zullen inkomen


page = requests.get(URL) # de html van de pagina opvragen
soup = BeautifulSoup(page.content, "html.parser") # de html van de pagina in een BeautifulSoup object steken

table = soup.find("table") # de tabel waarin alle categorieën staan opvragen
category_pages = table.findAll("a") # alle links binnen de tabel opvragen
category_pages = [requests.get(baseURL + category['href']) for category in category_pages]
# voor alle complete links de html opvragen, dit wordt gedaan door de href van de categorielink achter de baseURL te plakken 

all_image_page_URLs = []
# een lege lijst aanmaken waar alle pagina's van de images zullen inkomen

for category in category_pages:
    soup = BeautifulSoup(category.content, 'html.parser') # de html van de categorie in een BeautifulSoup object steken
    table = soup.find("table") # de tabel met alle links naar de pagina's van de images opvragen
    category_image_page_URLs = table.findAll("a") # alle links binnen deze tabel opvragen
    for image_page in category_image_page_URLs:
        all_image_page_URLs.append(image_page['href']) # de href van alle links in de lijst steken
    

for image_page_URL in all_image_page_URLs:
    category_tag = image_page_URL.split('/')[0] + '/' # de category tag is een deel van de complete url van de image die we nodig hebben
    page = requests.get(baseURL + image_page_URL) # de html opvragen van de pagina van een image
    soup = BeautifulSoup(page.content, 'html.parser') # de html van die pagina in een BeautifulSoup object steken
    imgs = soup.findAll('img')
    if len(imgs) == 0:
      continue
    # sommige links zijn dode links dus werk ik met een guard-clause die naar de volgende pagina gaat als er geen images gevonden worden op de huidige pagina
    img = imgs[-1]['src'] # ik vraag alle images op die pagina op en neem dan de laatste, omdat dat mij consistent de image die ik nodig heb geeft
    if(is_url_image(baseURL + category_tag + img)):
        img_URLs.append(baseURL + category_tag + img) # de complete url van de image opslaan in de lijst

img_URLs = list(set(img_URLs)) # de links die dubbel zijn opgeslagen verwijderen

locatie = '/schilderijen/rembrandt'
save_images(locatie, img_URLs)