import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from tensorflow.keras.callbacks import EarlyStopping


from tensorflow.keras.models import load_model
 
# load model
model = load_model('model11.h5')

classnames = ['cardboard','metal','paper','plastic','trash','green-glass','white-glass','brown-glass','clothes','biological','battery','shoes']

def predict_image(img):
  img_4d=img.reshape(-1,298, 384,3)
  prediction=model.predict(img_4d)[0]
  return {classnames[i]: float(prediction[i]) for i in range(12)}

sample_images = [
                 ["battery.JPG"],
                 ["jeans.jpg"],
                 ["paper1.jpg"]]
                

image = gr.inputs.Image(shape=(298, 384))
label = gr.outputs.Label(num_top_classes=3)

gr.Interface(fn=predict_image, inputs=image,  title="Garbage Classifier",
    description="This is the Model uploaded on Github trained on Dataset 11.This is just for a demo to test the deployment of Tensorflow Based Models into Gradio + Hugging Faces.",outputs=label,examples=sample_images,interpretation='default').launch(debug='True')