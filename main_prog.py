def warn(*args, **kwargs):
	pass
	import warnings
	warnings.warn = warn


import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import pickle

list1 = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
 'Tomato_Bacterial_spot' ,'Tomato_Early_blight' ,'Tomato_Late_blight',
 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite' ,'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']


image = Image.open('image (25).JPG')
image =image.resize(tuple((64,64)),Image.ANTIALIAS)
imagearray=img_to_array(image)
imagearray = np.expand_dims(imagearray,axis =0)


model = load_model("p_model.h5")
INIT_LR= 0.001
opt=Adam(learning_rate=INIT_LR)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])
prediction = model.predict(imagearray)


k=0
for i in range(15):
    val = prediction.item(i)
    if val==1:
        k = i
        list1[k]
        break

print(list1[k])

if(list1[k]=="Potato___Early_blight"):
    print("Valve of fertilizer will open")
    execfile('On-Off-Relay.py')

