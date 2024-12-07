from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Sentiment analysis function
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

# API route for sentiment analysis
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if text.strip():
        score, sentiment = get_sentiment_score(text)
        response = {
            "score": round(score, 2),
            "sentiment": sentiment
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Please provide some text for analysis"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
