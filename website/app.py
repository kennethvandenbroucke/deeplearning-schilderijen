from flask import Flask, render_template, request
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import keras
import numpy as np
import os

# de nodige functies importeren

app = Flask(__name__)
model = keras.models.load_model("modellen/VGG16.h5")

# de flask app aanmaken en het model al inladen, het model staat niet in de github omdat de size te groot is
if not os.path.exists('website/static'):
    os.mkdir('website/static')
if not os.path.exists('website/static/pics'):
    os.mkdir('website/static/pics')

picfolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picfolder

# een uploadfolder aanmaken, zodat we de opgeladen images kunnen weergeven

labels = ['Mondriaan', 'Picasso', 'Rembrandt', 'Rubens', 'VanGogh']


# de labels aanmaken zodat we van de vector voorspelling de klasse kunnen weergeven in text

@app.route('/')
def index():
    return render_template('index.html')

    # de home pagina, met als template index.html


@app.route('/predict', methods=['POST'])
def predict_image():
    image = request.files['image'].save('website/static/pics/image.jpeg')
    # de opgeladen image wordt uit de POST request gehaald en opgeslagen in de upload folder
    # deze image zal telkens overschreven worden, maar dat is niet erg want we willen toch maar één image tegelijk tonen
    # en dit bespaart opslagcapaciteit

    # de image preprocessen zoals we hebben gedaan toen we het model aanmaakten
    image = load_img('website/static/pics/image.jpeg', target_size=[256, 256])
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)

    # de voorspelling omzetten naar een van de klassen
    prediction = model.predict(image)
    print(prediction)
    [np.round(x) for x in prediction]
    prediction = np.argmax(prediction)
    prediction = labels[prediction]

    picture = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpeg')
    # het volledige pad naar de image in een variabele opslaan zodat we deze kunnen doorgeven aan de pagina die dit moet weergeven
    return render_template('prediction.html', prediction=prediction, image=picture)
    # de voorspelling en de images meegeven met de render_template functie die de image en de voorspelling zal tonen


if __name__ == '__main__':
    app.run()
    # de website opstarten
