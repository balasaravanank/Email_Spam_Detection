import streamlit as st
import joblib
import re
import numpy as np

# Load model and vectorizer with robust error handling
try:
    model = joblib.load('model.pkl')
    print("Model loaded successfully:", type(model))
    vectorizer = joblib.load('vectorizer.pkl')
    print("Vectorizer loaded successfully:", type(vectorizer))
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

# Custom CSS (Retaining all styles)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

body { background-color: #111b21; font-family: 'Arial', sans-serif; color: #ececec; }
.header { background-color: #232F3E; padding: 10px; color: white; text-align: center; margin-bottom: 20px; }
.title { font-size: 2.5em; margin: 0; }
.input-area {
    margin: 0 auto;
    max-width: 600px;
    padding: 20px;
    background-color: #1a242f;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.input-area textarea {
    user-select: all !important;
    -webkit-user-select: all !important;
    -moz-user-select: all !important;
    -ms-user-select: all !important;
    margin-top: 0px;
    resize: vertical;
    background-color: #1a242f;
    color: #ececec;
    border: 1px solid #343d49;
    overflow: auto;
    font-family: 'Roboto Mono', monospace;
    white-space: pre-wrap; /* For wrapping long text */
}
.prediction { font-size: 1.5em; font-weight: bold; text-align: center; margin-top: 20px; word-break: break-word; color: #ececec; }
.stButton>button {
    display: block;
    margin: 20px auto;
    background-image: linear-gradient(to right, #FFB347, #FF9800);
    border: none;
    color: #111b21;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.2s;
}
.stButton>button:hover {
    background-image: linear-gradient(to right, #FFA500, #FF8C00);
    transform: scale(1.05);
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    color: #111b21;
}
.stButton>button:active {
    transform: scale(0.95);
    box-shadow: none;
}
.footer { text-align: center; margin-top: 40px; color: #71797E; font-size: 0.9em; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection Using Logistic Regression</h1></div>', unsafe_allow_html=True)

# Input area (Only change is removing max_chars)
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...") # max_chars removed

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
st.markdown('<div class="footer"><p>Developed by <b>Your Name</b> | © 2024 Gmail Spam Detection System</p></div>', unsafe_allow_html=True)
