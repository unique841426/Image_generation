import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import os

client=InferenceClient(token="os.getenv("HF_TOKEN"))
Model="stabilityai/stable-diffusion-xl-base-1.0"

st.title("AI Image Generator")
st.write("Give your prompt to convert your imagination into image..")
prompt=st.text_input("Describe your image")

art_style = st.selectbox(
    "Select an art style:",
    ["Realistic", "Anime", "Cartoon"]
)

st.write("You selected:", art_style)



if st.button("generate") and prompt:
    with st.spinner("AI is generating your image..."):
       image=client.text_to_image(prompt,model=Model)
       st.image(image)


