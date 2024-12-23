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

# Custom CSS (Improved styling for professional look)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto:wght@400;700&display=swap');

body { background-color: #111b21; font-family: 'Roboto', sans-serif; color: #e0e0e0; } /* Changed font */
.header {
    background-color: #232F3E;
    padding: 20px 0; /* Reduced vertical padding, removed bottom margin */
    color: white;
    text-align: center;
    margin-bottom: 30px; /* Added margin below header */
}
.title { font-size: 2.2em; font-weight: 700; margin: 0; } /* Adjusted font size and weight */
.input-area {
    margin: 0 auto 30px; /* Added bottom margin to input area */
    max-width: 700px; /* Wider input area */
    padding: 25px;
    background-color: #1a242f;
    border-radius: 8px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Stronger shadow */
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
    padding: 10px; /* Added padding to textarea */
    font-size: 16px;
}
.prediction {
    font-size: 1.6em;
    font-weight: 700;
    text-align: center;
    margin-top: 25px;
    word-break: break-word;
}
.spam { color: #FF6B6B !important; } /* Red for spam */
.normal { color: #66BB6A !important; } /* Green for normal */
.stButton>button { /* Improved button styles */
    display: block;
    margin: 20px auto;
    background-image: linear-gradient(to right, #FFB347, #FF9800);
    border: none;
    color: #212121; /* Darker text */
    padding: 12px 25px;
    font-size: 17px;
    font-weight: 500;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s ease, transform 0.2s;
}
.stButton>button:hover {
    background-image: linear-gradient(to right, #FFA500, #FF8C00);
    transform: scale(1.02); /* Reduced scale */
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
}
.stButton>button:active {
    transform: scale(0.98);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}
.footer { text-align: center; margin-top: 40px; color: #757575; font-size: 0.9em; }
</style>
""", unsafe_allow_html=True)

# ... (Rest of the Streamlit app code - same as before)

                        if prediction[0] == 1:
                            st.markdown('<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True)
                        else:
                            st.markdown('<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True)

# ... (Rest of the Streamlit app code - same as before)
