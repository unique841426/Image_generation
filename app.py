import streamlit as st
from huggingface_hub import InferenceClient
from io import BytesIO
import os

client = InferenceClient(token=os.getenv("HF_TOKEN"))
Model = "stabilityai/stable-diffusion-xl-base-1.0"

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
            style_prompt = "ultra realistic, 8k, high detail, photorealistic"
        elif art_style == "Anime":
            style_prompt = "anime style, vibrant colors"
        elif art_style == "Cartoon":
            style_prompt = "cartoon style, colorful, 2D illustration"

        final_prompt = f"{prompt}, {style_prompt}"

        with st.spinner("Generating image..."):
            image = client.text_to_image(final_prompt, model=Model)

            # Show image
            st.image(image, caption=final_prompt)

            # 🔽 Convert image to bytes
            img_buffer = BytesIO()
            image.save(img_buffer, format="PNG")
            img_bytes = img_buffer.getvalue()

            # 🔽 Download button
            st.download_button(
                label="Download Image",
                data=img_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
