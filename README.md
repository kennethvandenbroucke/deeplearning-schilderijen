# deeplearning-schilderijen
## inhoud
Ik heb dit project in 5 delen opgedeeld:
1. webscraping
2. images controleren
3. kleinere dataset aanmaken
4. model trainen
5. website maken waarmee schilderijen kunnen voorspelt worden

## webscraping
voor de images van Rembrandt te verzamelen heb ik webscraping gedaan van deze site: http://www.rembrandtpainting.net/,
ik heb van die site 242 schilderijen van Rembrandt kunnen verzamelen.

## images controleren
Om te controleren op corruptie bij de images heb ik gebruikt gemaakt van de Image module binnen Pillow, als die module de image kan lezen
ga ik ervan uit dat de image niet corrupt is.

## kleinere dataset aanmaken
Een model op de volledige dataset trainen zou veel tijd in beslag nemen, daarom moeten modellen getraint worden op een kleiner deel van de schilderijen. De schilderijen worden eerst verdeeld in een train, test en validatieset. Daarna worden ze verder onderverdeelt volgens schilder. De hoeveelheid schilderijen kunnen worden bepaald voor elke schilder afzonderlijk.

## model trainen
Het model is getraint in een colaboratory notebook van google zodat gebruikt kan gemaakt worden van een GPU. Voor het trainen van het model wordt transfer learning gebruikt, ik haal de convolutional base op van het VGG16 model en haal er de bovenste laag van. Daarna train ik met een eigen classifier en gebruikt ik softmax als activatie, categorical_crossentropy als loss en RMSprop als optimizer.

## website
Voor de website maak ik gebruik van flask en html pagina's, je kan een schilderij van een van deze schilders uploaden:
1. Mondriaan
2. Picasso
3. Rembrandt
4. Rubens
als de vervolgens op submit drukt wordt het schilderij nog eens getoont en krijg je de voorspelling van het model te zien.
