import streamlit as st
import replicate
import os

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Genz Image AI", layout="centered")

st.title("🖼️ Genz – AI Image Generator")

# -------------------- API KEY --------------------
# Make sure you added this in Streamlit secrets:
# app2 = "your_replicate_api_key"
os.environ["REPLICATE_API_TOKEN"] = st.secrets["app2"]

# -------------------- INPUT --------------------
prompt = st.text_area("Enter your image prompt")

# -------------------- IMAGE GENERATION FUNCTION --------------------
def generate_image(prompt):
    output = replicate.run(
        "stability-ai/stable-diffusion",
        input={
            "prompt": prompt
        }
    )
    return output[0]

# -------------------- BUTTON --------------------
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... 🎨"):
            try:
                img_url = generate_image(prompt)

                # Show Image
                st.image(img_url, caption="Generated Image", use_column_width=True)

                # Save in session
                st.session_state.image = img_url

                st.success("Image generated successfully ✅")

            except Exception as e:
                st.error("Error generating image ❌")
                st.exception(e)
    else:
        st.warning("Please enter a prompt")

# -------------------- DOWNLOAD SECTION --------------------
if "image" in st.session_state:
    st.markdown("### 📥 Download Image")
    st.markdown(f"[Click here to download]({st.session_state.image})")
