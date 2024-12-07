import streamlit as st
import requests

# Streamlit UI
st.title("Sentiment Analysis App")

# User input
user_input = st.text_area("Enter your text for sentiment analysis:")

# Flask API URL
API_URL = "http://localhost:5000/predict"

if st.button("Predict"):
    if user_input.strip():
        # Sending request to Flask API
        response = requests.post(API_URL, json={"text": user_input})
        
        if response.status_code == 200:
            result = response.json()
            st.write(f"**Sentiment Score:** {result['score']}")
            st.write(f"**Overall Sentiment:** {result['sentiment']}")
        else:
            st.error(f"Error: {response.json()['error']}")
    else:
        st.warning("Please enter some text for analysis.")
