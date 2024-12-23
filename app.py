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

# Custom CSS (Brice SemiExpanded font)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto:wght@400;700&family=Bebas+Neue&display=swap'); /* Added Bebas Neue */

body { background-color: #111b21; font-family: 'Roboto', sans-serif; color: #e0e0e0; }
.header {
    padding: 20px 0;
    color: white;
    text-align: center;
    margin-bottom: 30px;
    background: none;
}
.title {
    font-size: 2.8em; /* Increased size */
    font-weight: 400; /* Adjusted weight for Bebas Neue */
    margin: 0;
    font-family: 'Bebas Neue', sans-serif; /* Use Bebas Neue for title */
    letter-spacing: 2px;
}
.input-area { /* ... (rest of the styles remain the same) */ }
.input-area textarea { /* ... */ }
.prediction { /* ... */ }
.spam { color: #FF6B6B !important; }
.normal { color: #66BB6A !important; }
.stButton>button { /* ... */ }
.footer { /* ... */ }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True) # Title changed

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...")

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
