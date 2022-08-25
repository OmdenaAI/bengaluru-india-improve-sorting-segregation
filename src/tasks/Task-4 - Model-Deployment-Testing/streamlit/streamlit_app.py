from cv2 import merge
import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
import pandas as pd
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
import keras.applications.vgg16 as vgg16
from keras.regularizers import l2

st.set_page_config(page_title="Image Segmentation",
                   page_icon="📝", layout="wide")

def main():
    header = st.container()
    desc = st.container()
    upload_image = st.container()
    show_image = st.container()
    image = None
    #img_size = 512
    width, height, channel = 224, 224, 3
    predict = False
    model = load_model('model')

    labels = ['battery','cardboard','clothes','food','glass','medical','metal','paper','plastic','shoes']

    with header:
        st.title("Waste Classification Project")

    with desc:
        st.markdown(""
        "")
        st.markdown(
            "The aim of this project is to develop image recognition techniques to improve the " 
            "sorting and segregation process of solid waste management. It comes under " 
            "SDG goals of 3 (Good Health & Well Being), 6(Clean Water & Sanitation) and "
            "11(Sustainable Cities & Communities)."
        )
        st.markdown(
            "10 types of waste can be classified in this project - battery, cardboard, clothes, food," 
            "glass, medical, metal, paper, plastic and shoes." 
        )

    with upload_image:
        image = st.file_uploader("Choose An Image File:", type=[
            "jpg", "png", "svg", "JPG", "jpeg", "JPEG"])

    with show_image:
        if image is not None:
            _, col2, _ = st.columns([3,6,3])
            with col2:
                st.image(image, caption = 'User Input', width = 500)
                predict = st.button('Predict the Category')
    
    if predict == True:
        image = Image.open(image)
        image = np.array(image.convert("RGB"))
        image = cv.resize(image, (width, height))
        img = image.reshape(-1, width, height, channel)
        pred = model.predict(img)[0]
        _, col2, _ = st.columns([2,6,2])
        with col2:
            st.subheader(f'output: {labels[np.argmax(pred)]}')
            chart_data = pd.DataFrame(
                pred,index=labels)
            st.bar_chart(chart_data)

if __name__ == "__main__":
    main()
