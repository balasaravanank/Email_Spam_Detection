import streamlit as st
import joblib
import re
import numpy as np

# ... (Load model and vectorizer, clean_text function - same as before)

# Custom CSS (Button styling and gradient)
st.markdown("""
<style>
body { background-color: #f7f7f7; font-family: 'Arial', sans-serif; }
/* ... (other styles - same as before) */
.input-area textarea { user-select: auto; -webkit-user-select: auto; -moz-user-select: auto; -ms-user-select: auto; }
.prediction { font-size: 1.5em; font-weight: bold; text-align: center; margin-top: 20px; word-break: break-word; }
.stButton>button { /* Center and style the button */
    display: block;
    margin: 20px auto; /* Center horizontally */
    background-image: linear-gradient(to right, #FFB347, #FF9800); /* Sunset gradient */
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease; /* Smooth transition */
}
.stButton>button:hover {
    background-image: linear-gradient(to right, #FF9800, #FF8F00); /* Darker shade on hover */
}
</style>
""", unsafe_allow_html=True)

# ... (Header - same as before)

# Input area
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    user_input = st.text_area("Enter your message:", height=200, key="input_text", help="Type your message here...", placeholder="Type your message here...", max_chars=500)

    if st.button("Predict", key="predict_button"): # Button is now styled
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
                            st.markdown(f'<p class="prediction spam">Prediction: Spam</p>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<p class="prediction normal">Prediction: Normal Mail</p>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# ... (Footer - same as before)
