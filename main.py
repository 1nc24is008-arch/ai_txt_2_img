import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Genz Image AI", layout="centered")

st.title("🖼️ Genz – AI Image Generator")

# Input prompt
prompt = st.text_area("Enter your image prompt")

# Function to generate image
def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {
        "Authorization": f"Bearer {st.secrets['new']}"
    }

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return response.content
    else:
        return None

# Button
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... 🎨"):
            img = generate_image(prompt)

            if img:
                st.image(img, caption="Generated Image", use_column_width=True)

                # Save to session
                st.session_state.image = img

                st.success("Image generated successfully ✅")
            else:
                st.error("Failed to generate image ❌")
    else:
        st.warning("Please enter a prompt")

# Download option
if "image" in st.session_state:
    st.download_button(
        label="⬇️ Download Image",
        data=st.session_state.image,
        file_name="ai_image.png",
        mime="image/png"
    )
