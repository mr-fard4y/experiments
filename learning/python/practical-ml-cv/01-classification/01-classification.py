import tensorflow as tf
from tensorflow.keras.applications.resnet50 import (
    preprocess_input, decode_predictions
)
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import pprint


def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    model = tf.keras.applications.resnet50.ResNet50()
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    pprint.pprint(decode_predictions(prediction, top=3)[0])


IS_COLAB_ENV = False
try:
    import google.colab
    IS_COLAB_ENV = True
except Exception as ex:
    pass

model = tf.keras.applications.resnet50.ResNet50()


PATHES = ['../examples/cat.png', '../examples/dog-2.png']
for img_path in PATHES:
    img = image.load_img(img_path, target_size=(224, 224))
    plt.imshow(img)
    plt.show()

    predict(img_path)
