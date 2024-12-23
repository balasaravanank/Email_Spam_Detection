# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd
import re
import time

# Load the pre-trained model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except Exception as e:
    st.error("Error loading model or vectorizer. Please check the files.")
    st.stop()

# Function to clean input text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
    }
    .header {
        background-color: #232F3E;
        padding: 10px;
        color: white;
        text-align: center;
    }
    .title {
        font-size: 2.5em;
        margin: 0;
    }
    .input-area {
        margin: 20px auto;
        max-width: 600px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .prediction {
        font-size: 1.5em;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .button {
        background-color: #FF9900;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        display: inline-block;
        text-align: center;
        margin-top: 10px;
    }
    .button:hover {
        background-color: #e68a00;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200)
    
    if st.button("Predict"):
        if not user_input:
            st.error("Please enter a message to predict.")
        else:
            with st.spinner("Processing..."):
                time.sleep(1)  # Simulate processing time
                cleaned_input = clean_text(user_input)  # Clean the input
                # Vectorize the cleaned input
                input_vectorized = vectorizer.transform([cleaned_input])  # Reshape to 2D array
                prediction = model.predict(input_vectorized)  # Make prediction
                
                # Display result
                if prediction[0] == 1:
                    st.markdown('<p class="prediction">Prediction: Spam</p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p class="prediction">Prediction: Normal Mail</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>&copy; 2024 Sreesanth R. All rights reserved.</p></div>', unsafe_allow_html=True)
