import os, requests

def save_images(folder, urls):
    if not os.path.exists(folder):
        os.makedirs(folder) # als de opslaglocatie nog niet bestaat, de opslaglocatie aanmaken
    for index, URL in enumerate(urls):
        image = requests.get(URL).content # de data van de image opvragen
        with open(f'{folder}/{index}.jpg', 'wb') as handler:
            handler.write(image)
        
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False
   # deze functie kijkt of een van de image-formaten in de header staat van een link en geeft True terug als dat zo is, anders False