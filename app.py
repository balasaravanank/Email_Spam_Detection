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
    st.stop()

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Custom CSS
st.markdown("""
<style>
body { background-color: #f7f7f7; font-family: 'Arial', sans-serif; }
.header { background-color: #232F3E; padding: 10px; color: white; text-align: center; }
.title { font-size: 2.5em; margin: 0; }
.input-area { margin: 20px auto; max-width: 600px; padding: 20px; background-color: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
.input-area textarea { user-select: auto; -webkit-user-select: auto; -moz-user-select: auto; -ms-user-select: auto; }
.prediction { font-size: 1.5em; font-weight: bold; text-align: center; margin-top: 20px; word-break: break-word; }
.stButton>button {
    display: block;
    margin: 20px auto;
    background-image: linear-gradient(to right, #FFB347, #FF9800);
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-image: linear-gradient(to right, #FF9800, #FF8F00);
}
.footer { text-align: center; margin-top: 40px; color: gray; font-size: 0.9em; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1 class="title">Gmail Spam Detection</h1></div>', unsafe_allow_html=True)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)  # Opening div
    user_input = st.text_area("Enter your message:", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...", max_chars=500)

    if st.button("Predict", key="predict_button"):
        if not user_input.strip():
            st.error("Please enter a message to predict.")
        else:
            with st.spinner('Processing...'):
                cleaned_input = clean_text(user_input)
                input_vectorized = vectorizer.transform([cleaned_input])

                if input_vectorized.shape[0] == 0:
                    st.warning("The input text did not contain any recognizable words for the model.")
                else:
                    try:
                        prediction = model.predict(input_vectorized)
                        if prediction[0] == 1:
                            st.markdown('<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True) #Corrected line
                        else:
                            st.markdown('<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True) #Corrected line
                    except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")

    st.markdown('</div>', unsafe_allow_html=True)  # Closing div

# Footer
st.markdown('<div class="footer"><p>Developed by <b>Your Name</b> | © 2024 Gmail Spam Detection System</p></div>', unsafe_allow_html=True)
