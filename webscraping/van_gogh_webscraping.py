import requests
from bs4 import BeautifulSoup
from webscraping_functions import save_images, is_url_image

# requests is nodig om de html van de pagina's te verkrijgen
# BeautifulSoup wordt gebruikt om gemakkelijk elementen van de html te kunnen verkrijgen

URL = 'http://www.vggallery.com/painting/main_az.htm'  # de URL van de beginpagina
baseURL = 'http://www.vggallery.com/painting/'
# de basis van alle URL's van de site, deze is nodig omdat de links van alle paginas
# relatief zijn, hiermee kan de volledige URL gemaakt worden.

img_URLs = []  # een lege lijst aanmaken waar alle URLs zullen inkomen

page = requests.get(URL)  # de html van de pagina opvragen
soup = BeautifulSoup(page.content, "html.parser")  # de html van de pagina in een BeautifulSoup object steken

table = soup.find_all("table")[1]  # de tabel waarin alle categorieën staan opvragen
category_pages = table.findAll("a")  # alle links binnen de tabel opvragen
category_pages = [requests.get(baseURL + category['href']) for category in category_pages]

# voor alle complete links de html opvragen, dit wordt gedaan door de href van de categorielink achter de baseURL te plakken

all_image_page_URLs = []
# een lege lijst aanmaken waar alle pagina's van de images zullen inkomen

for category in category_pages:
    soup = BeautifulSoup(category.content, 'html.parser')  # de html van de categorie in een BeautifulSoup object steken
    table = soup.find("table")  # de tabel met alle links naar de pagina's van de images opvragen
    category_image_page_URLs = table.findAll("a")  # alle links binnen deze tabel opvragen
    for image_page in category_image_page_URLs:
        all_image_page_URLs.append(image_page['href'])  # de href van alle links in de lijst steken

for image_page_URL in all_image_page_URLs:
    page = requests.get(baseURL + image_page_URL)  # de html opvragen van de pagina van een image
    soup = BeautifulSoup(page.content, 'html.parser')  # de html van die pagina in een BeautifulSoup object steken
    imgs = soup.find_all('img')
    img = imgs[2]
    if is_url_image(baseURL + img['src']):
        img_URLs.append(baseURL + img['src'])  # de complete url van de image opslaan in de lijst

img_URLs = list(set(img_URLs))  # de links die dubbel opgeslaan zijn verwijderen

save_images('/content/drive/MyDrive/deeplearning/schilderijen/VanGogh', img_URLs)
