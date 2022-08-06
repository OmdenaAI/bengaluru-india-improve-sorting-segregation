import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow.keras as keras
import keras.applications.mobilenet_v2 as mobilenetv2

from tensorflow.keras.models import load_model
 
# load model
model = load_model('model18.h5')

classnames = ['battery','biological','brown-glass','cardboard','clothes','green-glass','metal','paper','plastic','shoes','trash','white-glass']



def predict_image(img):
  img_4d=img.reshape(-1,224, 224,3)
  prediction=model.predict(img_4d)[0]
  return {classnames[i]: float(prediction[i]) for i in range(12)}

                

image = gr.inputs.Image(shape=(224, 224))
label = gr.outputs.Label(num_top_classes=3)
article="<p style='text-align: center'>Made by Aditya Narendra with 🖤</p>"
examples = ['battery.jpeg','cardboard.jpeg','paper.jpg','clothes.jpeg','metal.jpg','plastic.jpg','shoes.jpg']


gr.Interface(fn=predict_image, inputs=image,  title="Garbage Classifier V3",
    description="This is a Garbage Classification Model Trained using MobileNetV2.Deployed to Hugging Faces using Gradio.",outputs=label,examples=examples,article=article,enable_queue=True,interpretation='default').launch(share="True")