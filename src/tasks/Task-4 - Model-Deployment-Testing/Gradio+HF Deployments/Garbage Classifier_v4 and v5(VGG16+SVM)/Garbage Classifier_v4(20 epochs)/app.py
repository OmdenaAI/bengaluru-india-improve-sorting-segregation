import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow.keras as keras
import keras.applications.vgg16 as vgg16

from tensorflow.keras.models import load_model
 
# load model
model = load_model('model6904.h5')

classnames = ['battery','cardboard','clothes','food','glass','medical','metal','paper','plastic','shoes']



def predict_image(img):
  img_4d=img.reshape(-1,224, 224,3)
  prediction=model.predict(img_4d)[0]
  return {classnames[i]: float(prediction[i]) for i in range(10)}

                

image = gr.inputs.Image(shape=(224, 224))
label = gr.outputs.Label(num_top_classes=3)
article="<p style='text-align: center'>Made by Aditya Narendra with 🖤</p>"



gr.Interface(fn=predict_image, inputs=image,  title="Garbage Classifier V4-VGG16+SVM",
    description="This is a Garbage Classification Model Trained using VGG16+SVM(20 Epochs).Deployed to Hugging Faces using Gradio.",outputs=label,article=article,enable_queue=True,interpretation='default').launch(share="True")