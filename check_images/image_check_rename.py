from PIL import Image
import os

schilderijen_folder = "/content/drive/MyDrive/deeplearning/schilderijen"

painter_directories = os.listdir(schilderijen_folder) # de folders van alle painters in een lijst verzamelen
for painter_directory in painter_directories:
  index = 0 # index die zal gebruikt worden voor de naam van de file
  for image in os.listdir(f"{schilderijen_folder}/{painter_directory}"):
      with Image.open(f"{schilderijen_folder}/{painter_directory}/{image}") as img:
        os.remove(f"{schilderijen_folder}/{painter_directory}/{image}") # de originele verwijderen
        # alle images binnen de folder van de schilder openen om te controleren of ze corrupt zijn en ze te hernoemen
        img.convert('RGB').save(f'{schilderijen_folder}/{painter_directory}/{index}.jpg', "JPEG")
        # de images opslaan
      index+=1
        # de index verhogen anders worden de opgeslagen images telkens overschreven