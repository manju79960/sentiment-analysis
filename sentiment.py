import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# ---------------------
# Clean text
# ---------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


# ---------------------
# Emotion detection
# ---------------------

def detect_emotion(text):

    text = clean_text(text)

    emotions = {

    "😄 Happy": [
        "happy","joy","excited","great","love","amazing","wonderful","interesting",
        "beautiful","enjoyed","awesome","fantastic","good","nice","excellent",
        "delighted","pleased","glad","smile","fun","perfect","brilliant"
    ],

    "😡 Angry": [
        "angry","furious","hate","annoyed","irritated","mad","frustrated",
        "upset","disgusted","rage","irritating","bad","terrible","worst",
        "unfair","disappointed","complain"
    ],

    "😢 Sad": [
        "sad","depressed","unhappy","cry","heartbroken","lonely","miserable",
        "down","hurt","sorrow","gloomy","pain","tired","hopeless"
    ],

    "😨 Fear": [
        "fear","scared","afraid","terrified","nervous","difficult","worried",
        "anxious","panic","danger","stress","scary","threat","risk"
    ],

    "😲 Surprise": [
        "surprised","shocked","wow","unexpected","unbelievable",
        "astonished","amazed","suddenly","incredible","strange"
    ]
}
    for emotion, keywords in emotions.items():
        if any(word in text for word in keywords):
            return emotion

    return "😐 Neutral Emotion"


# ---------------------
# Sentiment analysis
# ---------------------

def analyze_sentiment(text):

    cleaned = clean_text(text)

    scores = sia.polarity_scores(cleaned)

    compound = scores['compound']
    pos = scores['pos']
    neg = scores['neg']
    neu = scores['neu']

    if compound >= 0.2:
        sentiment = "😊 Positive"
        color = "#22c55e"

    elif compound <= -0.2:
        sentiment = "😞 Negative"
        color = "#ef4444"

    else:
        sentiment = "😐 Neutral"
        color = "#facc15"

    emotion = detect_emotion(text)

    return sentiment, color, compound, pos, neg, neu, emotion