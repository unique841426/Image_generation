import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import os

client = InferenceClient(token=os.getenv("HF_TOKEN"))
Model = "stabilityai/stable-diffusion-xl-base-1.0"

st.title("AI Image Generator 🚀")
st.write("Give your prompt to convert your imagination into image..")

prompt = st.text_input("Describe your image")

art_style = st.selectbox(
    "Select an art style:",
    ["Realistic", "Anime", "Cartoon"]
)

st.write("You selected:", art_style)

# 🎨 Style mapping
style_map = {
    "Realistic": "ultra realistic, 8k, high detail",
    "Anime": "anime style, vibrant colors",
    "Cartoon": "cartoon style, 2D illustration"
}

if st.button("generate") and prompt:
    with st.spinner("AI is generating your image..."):

        # ✅ style apply
        final_prompt = f"{prompt}, {style_map[art_style]}"

        image = client.text_to_image(
            final_prompt,
            model=Model
        )

        # ✅ show image
        st.image(image, caption=final_prompt)

        # ✅ download option
        import io
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")

        st.download_button(
            label="Download Image",
            data=img_bytes.getvalue(),
            file_name="generated_image.png",
            mime="image/png"
        )
