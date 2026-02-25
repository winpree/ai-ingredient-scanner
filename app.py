import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# 1. Setup API Key (In a real app, use environment variables!)
os.environ["GOOGLE_API_KEY"] = " "
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 2. Initialize the Gemini Model (The 'Brain')
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. Streamlit UI Elements
st.set_page_config(page_title="AI Chef Scanner", page_icon="🥗")
st.header("📸 Smart Ingredient Scanner")
st.write("Upload a photo of your ingredients, and I'll tell you what to cook!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    submit = st.button("Identify & Get Recipes")

    # 4. Logic for Analysis
    if submit:
        # The 'Prompt' tells the AI exactly how to behave
        prompt = """
        You are an expert chef. Look at this image and:
        1. List every ingredient you can identify.
        2. Suggest 3 quick recipes that can be made using these items.
        3. Format the response clearly with bullet points and bold headers.
        """
        
        with st.spinner('Analyzing your fridge...'):
            # Send the image and prompt to the AI
            response = model.generate_content([prompt, image])
            
            st.subheader("👨‍🍳 Chef's Recommendation:")
            st.write(response.text)
