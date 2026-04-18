import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Genz Image AI", layout="centered")

st.title("🖼️ Genz – AI Image Generator (FREE)")

# -------------------- API CONFIG --------------------
# Get your free token from Hugging Face
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {
    "Authorization": "Bearer YOUR_HF_TOKEN"   # 🔑 Replace this
}

# -------------------- INPUT --------------------
prompt = st.text_area("Enter your image prompt")

# -------------------- FUNCTION --------------------
def generate_image(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )
    return response.content

# -------------------- BUTTON --------------------
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... 🎨"):
            try:
                image_bytes = generate_image(prompt)

                # Show image
                st.image(image_bytes, caption="Generated Image")

                # Save to session
                st.session_state.image = image_bytes

                st.success("Image generated successfully ✅")

            except Exception as e:
                st.error("Error generating image ❌")
                st.exception(e)
    else:
        st.warning("Please enter a prompt")

# -------------------- DOWNLOAD --------------------
if "image" in st.session_state:
    st.download_button(
        label="📥 Download Image",
        data=st.session_state.image,
        file_name="generated_image.png",
        mime="image/png"
    )
