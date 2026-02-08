from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the text.
    Returns a tuple: (polarity, label)
    Polarity: -1.0 (Very Negative) to 1.0 (Very Positive)
    Label: POSITIVE, NEUTRAL, NEGATIVE
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        return polarity, "POSITIVE"
    elif polarity < -0.1:
        return polarity, "NEGATIVE"
    else:
        return polarity, "NEUTRAL"

if __name__ == "__main__":
    tests = ["I love programming!", "This is the worst day ever.", "I am eating an apple."]
    for t in tests:
        p, l = analyze_sentiment(t)
        print(f"'{t}' -> {l} ({p:.2f})")
