import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Genz Image AI", layout="centered")

st.title("🖼️ Genz – AI Image Generator")

# -------------------- API CONFIG --------------------
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {
    "Authorization": "Bearer Dear_AI"   # 🔑 PUT YOUR TOKEN HERE
}

# -------------------- INPUT --------------------
prompt = st.text_area("Enter your image prompt")

# -------------------- FUNCTION --------------------
def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.content

# -------------------- BUTTON --------------------
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... 🎨"):
            try:
                image_bytes = generate_image(prompt)
                st.image(image_bytes)

                st.session_state.image = image_bytes
                st.success("Image generated ✅")

            except Exception as e:
                st.error("Error ❌")
                st.exception(e)
    else:
        st.warning("Enter a prompt")

# -------------------- DOWNLOAD --------------------
if "image" in st.session_state:
    st.download_button(
        "📥 Download",
        data=st.session_state.image,
        file_name="image.png",
        mime="image/png"
    )
