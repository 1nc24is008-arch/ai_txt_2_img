import streamlit as st
import requests

st.set_page_config(page_title="Genz Image AI", layout="centered")
st.title("🖼️ Genz – AI Image Generator")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {
    "Authorization": "Dear_AI"
}

prompt = st.text_area("Enter your image prompt")

def generate_image(prompt):
    return requests.post(API_URL, headers=headers, json={"inputs": prompt})

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... 🎨"):
            try:
                response = generate_image(prompt)

                # ✅ CASE 1: IMAGE SUCCESS
                if response.status_code == 200 and "image" in response.headers.get("content-type", ""):
                    st.image(response.content)
                    st.session_state.image = response.content
                    st.success("Image generated ✅")

                # ❌ CASE 2: ERROR RESPONSE
                else:
                    st.error("API Error ❌")

                    try:
                        st.write(response.json())  # if JSON
                    except:
                        st.write(response.text)   # if not JSON

            except Exception as e:
                st.error("Error ❌")
                st.exception(e)
    else:
        st.warning("Enter a prompt")

# DOWNLOAD
if "image" in st.session_state:
    st.download_button(
        "📥 Download",
        data=st.session_state.image,
        file_name="image.png",
        mime="image/png"
    )
