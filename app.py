import streamlit as st
import joblib
import re
import numpy as np

# Load model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    st.error("Model or vectorizer files not found. Please ensure 'model.pkl' and 'vectorizer.pkl' are in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    print(f"Detailed error: {e}")
    st.stop()

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Streamlit app
st.set_page_config(page_title="Gmail Spam Detection", page_icon="✉️")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto:wght@400;700&family=Bebas+Neue&display=swap');

body { background-color: #111b21; font-family: 'Roboto', sans-serif; color: #e0e0e0; }
.header {
    padding: 20px 0;
    color: white;
    text-align: center;
    margin-bottom: 30px;
    background: none;
}
.title {
    font-size: 2.8em;
    font-weight: 400;
    margin: 0;
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 2px;
}
.input-area {
    margin: 0 auto 30px;
    max-width: 700px;
    padding: 25px;
    background-color: #1a242f;
    border-radius: 8px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}
.input-area label {
    display: block;
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.2em;
}
.input-area textarea {
    user-select: all !important;
    -webkit-user-select: all !important;
    -moz-user-select: all !important;
    -ms-user-select: all !important;
    margin-top: 0px;
    resize: vertical;
    background-color: #1a242f;
    color: #e0e0e0;
    border: 1px solid #343d49;
    overflow: auto;
    font-family: 'Roboto Mono', monospace;
    padding: 10px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
}
.prediction {
    font-size: 2em;
    font-weight: 700;
    text-align: center;
    margin-top: 25px;
    word-break: break-word;
}
.spam { color: #FF6B6B !important; }
.normal { color: #66BB6A !important; }
.stButton {
    display: flex;
    justify-content: center;
}
.stButton>button {
    display: block;
    margin: 20px 0;
    background-image: linear-gradient(to right, #FFB347, #FF9800);
    border: none;
    color: #212121;
    padding: 12px 25px;
    font-size: 17px;
    font-weight: 500;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s ease, transform 0.2s;
}
.stButton>button:hover {
    background-image: linear-gradient(to right, #FFA500, #FF8C00);
    transform: scale(1.02);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
    color: #212121;
}
.stButton>button:active {
    transform: scale(0.98);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}
.footer { text-align: center; margin-top: 40px; color: #757575; font-size: 0.9em; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter Your Mail", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...") # Changed label text

    if st.button("Predict", key="predict_button"):
        if not user_input.strip():
            st.error("Please enter a message to predict.")
        else:
            with st.spinner('Processing...'):
                cleaned_input = clean_text(user_input)
                print("Cleaned Input:", cleaned_input)
                try:
                    input_vectorized = vectorizer.transform([cleaned_input])
                    print("Vectorized Input Shape:", input_vectorized.shape)
                    if input_vectorized.shape[0] == 0:
                        st.warning("The input text did not contain any recognizable words for the model.")
                    else:
                        prediction = model.predict(input_vectorized)
                        print("Raw Prediction:", prediction)
                        if prediction[0] == 1:
                            st.markdown('<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True)
                        else:
                            st.markdown('<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")
                    print(f"Detailed prediction error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f'<div class="footer"><p>Developed by <b>Bala Saravanan K> | © 2024 Gmail Spam Detection System</p></div>', unsafe_allow_html=True)
