import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model("model_malaria_detection.h5")


def process_image(img):
    img = img.convert("RGB")
    img = img.resize((50, 50))
    img = np.array(img)
    if img.ndim == 2:
        img = np.stack((img,) * 3, axis=-1)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


st.title("MALARIA RECOGNITION")
st.divider()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("malaria.jpeg")
st.divider()

st.success(
    "Upload your malaria image from blood cell and classify the images with the following labels: Uninfected and Parasitized with CNN deep learning.")
st.divider()

st.write("Upload your image and see the results")
st.divider()

file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "webp"])

if file is not None:
    img = Image.open(file)
    st.image(img, caption="Uploaded image")
    image = process_image(img)
    prediction = model.predict(image)
    predicted_class = np.round(prediction)
    predicted_class = predicted_class.flatten()
    print(type(predicted_class), predicted_class.shape)

    class_names = {0: "Parasitized", 1: "Uninfected"}

    st.write(f"Predicted Malaria Type: {class_names[predicted_class]}")