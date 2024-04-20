import streamlit as st 
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np


model = load_model("skin_cancer_model.h5")

def process_image(img):
    img = img.resize((170,170))
    img = np.array(img)
    img = img/255.0
    img = np.expand_dims(img,axis=0)
    return img

st.title("SKIN CANCER CLASSIFICATION:cancer:")
st.write("Upload your image and see the results")

file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])

if file is not None:
    img = Image.open(file)
    st.image(img, caption="Downloaded image")
    image=process_image(img)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    
    class_names = ["Not Cancer","Cancer"]
    st.write(class_names[predicted_class])