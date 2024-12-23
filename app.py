# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd
import re
import time

# Load the pre-trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

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
        background-color: #f0f2f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: #ff6b39;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .prediction {
        font-size: 1.5em;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .input-area {
        margin: 20px auto;
        max-width: 600px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit application
st.markdown('<h1 class="title">Gmail Spam Detection Using Logistic Regression</h1>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200)
    if st.button("Predict"):
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
st.markdown("""
    <footer style="text-align: center; margin-top: 40px;">
        <p style="color: gray;">&copy; 2024 Sreesanth R. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
