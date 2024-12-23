# Import necessary libraries
import streamlit as st
import joblib
import re
import time

# Load the pre-trained model and vectorizer
try:
    model = joblib.load('model.pkl')  # Ensure this file is in the same directory
    vectorizer = joblib.load('vectorizer.pkl')  # Ensure this file is in the same directory
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

# Custom CSS for styling and spinner
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
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .spam {
        color: red;
    }
    .normal {
        color: green;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
        font-size: 0.9em;
    }
    .spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50px;
        margin: 10px auto;
    }
    .dot {
        width: 10px;
        height: 10px;
        margin: 0 5px;
        background-color: #0078D7;
        border-radius: 50%;
        animation: blink 1.5s infinite ease-in-out;
    }
    .dot:nth-child(2) {
        animation-delay: 0.3s;
    }
    .dot:nth-child(3) {
        animation-delay: 0.6s;
    }
    @keyframes blink {
        0%, 80%, 100% {
            opacity: 0;
        }
        40% {
            opacity: 1;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Spinner HTML
spinner_html = """
<div class="spinner">
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
</div>
"""

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area(
        "Enter your message:", 
        height=200, 
        key="input_text", 
        help="Type your message here...", 
        placeholder="Type your message here...", 
        max_chars=500
    )
    
    if st.button("Predict", key="predict_button"):
        if not user_input:
            st.error("Please enter a message to predict.")
        else:
            st.markdown(spinner_html, unsafe_allow_html=True)  # Show spinner
            time.sleep(2)  # Simulate processing time
            cleaned_input = clean_text(user_input)  # Clean the input
            try:
                input_vectorized = vectorizer.transform([cleaned_input])  # Vectorize input
                prediction = model.predict(input_vectorized)  # Make prediction
                st.markdown(spinner_html, unsafe_allow_html=False)  # Remove spinner after processing
                if prediction[0] == 1:
                    st.markdown('<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Developed by <b>Sreesanth R</b> | © 2024 Gmail Spam Detection System</p>
    </div>
""", unsafe_allow_html=True)
