# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd
import re

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

# Streamlit application
st.title("Gmail Spam Detection Using Logistic Regression")
user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    cleaned_input = clean_text(user_input)  # Clean the input
    # Vectorize the cleaned input
    input_vectorized = vectorizer.transform([cleaned_input])  # Reshape to 2D array
    prediction = model.predict(input_vectorized)  # Make prediction
    st.write("Prediction:", "Spam" if prediction[0] == 1 else "Ham")  # Display result
