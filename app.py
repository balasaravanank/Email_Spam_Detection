import streamlit as st
import joblib
import re
import time
import numpy as np  # Import numpy for handling empty vectors

# Load the pre-trained model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    st.error("Model or vectorizer files not found. Please ensure 'model.pkl' and 'vectorizer.pkl' are in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Function to clean input text (Improved regex)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # More robust URL removal
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Keep only alphanumeric and spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Custom CSS (Slightly refined)
st.markdown("""
<style>
body { background-color: #f7f7f7; font-family: 'Arial', sans-serif; }
.header { background-color: #232F3E; padding: 10px; color: white; text-align: center; }
.title { font-size: 2.5em; margin: 0; }
.input-area { margin: 20px auto; max-width: 600px; padding: 20px; background-color: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
.prediction { font-size: 1.5em; font-weight: bold; text-align: center; margin-top: 20px; } /* Reduced font size a bit*/
.spam { color: red; }
.normal { color: green; }
.footer { text-align: center; margin-top: 40px; color: gray; font-size: 0.9em; }
.loader { border: 8px solid #f3f3f3; border-top: 8px solid #3498db; border-radius: 50%; width: 50px; height: 50px; animation: spin 2s linear infinite; margin: 20px auto;}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...", max_chars=500)

    if st.button("Predict", key="predict_button"):
        if not user_input.strip(): # Check for empty or whitespace-only input
            st.error("Please enter a message to predict.")
        else:
            with st.spinner('Processing...'):  # Use Streamlit's built-in spinner
                cleaned_input = clean_text(user_input)
                input_vectorized = vectorizer.transform([cleaned_input])

                # Handle empty vectorized input
                if input_vectorized.shape[0] == 0:
                    st.warning("The input text did not contain any recognizable words for the model.")
                else:
                    try:
                        prediction = model.predict(input_vectorized)
                        if prediction[0] == 1:
                            st.markdown('<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True)
                        else:
                            st.markdown('<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>Developed by <b>Your Name</b> | © 2024 Gmail Spam Detection System</p></div>', unsafe_allow_html=True)
