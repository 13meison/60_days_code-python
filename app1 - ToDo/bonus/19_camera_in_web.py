import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    #Start the camera
    camera = st.camera_input('Input')
    print(camera)

    if camera:
        #Create pillow image instanse
        img = Image.open(camera)
        #Convert image
        gray_img = img.convert('L')
        #Render image to landscape
        st.image(gray_img)

with st.expander('Upload and convert app'):
    uploaded_image = st.file_uploader("Upload Image")
    if uploaded_image:
        img = Image.open(uploaded_image)
        # Convert image
        gray_img = img.convert('L')
        # Render image to landscape
        st.image(gray_img)