from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt


PATH_TO_MODEL = "model.h5"
model = load_model(PATH_TO_MODEL)


def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    print(prediction)


PATHES = ['../examples/cat.png', '../examples/dog-2.png']
for img_path in PATHES:
    img = image.load_img(img_path, target_size=(224, 224))
    plt.imshow(img)
    plt.show()

    predict(img_path)
