import streamlit as st
from PIL import Image
import numpy as np

st.title("🎈testing that camera function")

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    img = np.array(img)
    st.image(img)

st.write("supposedly this does something")
