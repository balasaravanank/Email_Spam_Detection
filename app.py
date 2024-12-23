# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd
import re

# Load the pre-trained model
model = joblib.load('model.pkl')

# Function to clean input text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Streamlit application
st.title("Gmail Spam Detection Using Logistic Regression")
user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    cleaned_input = clean_text(user_input)  # Clean the input
    prediction = model.predict([cleaned_input])  # Make prediction
    st.write("Prediction:", "Spam" if prediction[0] == 1 else "Ham")  # Display result
