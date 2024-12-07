import streamlit as st
from textblob import TextBlob

# Streamlit app
st.title("Sentiment Analysis App")

# Check if the app is being accessed as an API
api_call = st.experimental_get_query_params().get('api', [None])[0]

# Function to analyze sentiment
def get_sentiment_score(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment_score, sentiment

if api_call == "true":
    st.write("API mode enabled")
    # Extract JSON input
    input_json = st.text_area("Paste JSON input here:")
    if st.button("Predict from API"):
        try:
            input_data = json.loads(input_json)
            text = input_data["text"]
            score, sentiment = get_sentiment_score(text)
            st.json({
                "sentiment_score": round(score, 2),
                "sentiment": sentiment
            })
        except Exception as e:
            st.error(f"Error parsing input: {e}")
else:
    st.write("Interactive mode enabled. Enter text below:")

    # User input section
    user_input = st.text_area("Enter your text for sentiment analysis:")

    # Button to make a prediction
    if st.button("Predict"):
        if user_input.strip():
            # Get sentiment score and sentiment
            score, sentiment = get_sentiment_score(user_input)

            # Display results
            st.write(f"**Sentiment Score:** {round(score, 2)}")
            st.write(f"**Overall Sentiment:** {sentiment}")
        else:
            st.warning("Please enter some text for analysis.")
