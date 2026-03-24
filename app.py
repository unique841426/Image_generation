import streamlit as st
import replicate
from io import BytesIO
from PIL import Image
import requests
import os

st.title("AI Image Generator")

prompt = st.text_input("Describe your image")

art_style = st.selectbox(
    "Select an art style:",
    ["Realistic", "Anime", "Cartoon"]
)

if st.button("Generate"):
    if not prompt:
        st.warning("Please enter a prompt first!")
    else:
        # Style mapping
        if art_style == "Realistic":
            style_prompt = "ultra realistic, 8k, high detail"
        elif art_style == "Anime":
            style_prompt = "anime style, vibrant colors"
        elif art_style == "Cartoon":
            style_prompt = "cartoon style, 2D illustration"

        final_prompt = f"{prompt}, {style_prompt}"

        with st.spinner("Generating image..."):
            output = replicate.run(
                "stability-ai/sdxl:latest",
                input={"prompt": final_prompt}
            )

            image_url = output[0]

            # Convert URL to image
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))

            # Show image
            st.image(image, caption=final_prompt)

            # Download
            img_buffer = BytesIO()
            image.save(img_buffer, format="PNG")
            st.download_button(
                label="Download Image",
                data=img_buffer.getvalue(),
                file_name="generated_image.png",
                mime="image/png"
            )
