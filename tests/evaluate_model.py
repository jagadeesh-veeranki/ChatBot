import json
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils.nlp_utils import preprocess

def clean_text(text):
    tokens = preprocess(text)
    return " ".join(tokens)

def evaluate():

    data_file = os.path.join(os.path.dirname(__file__), '../data/intents.json')
    with open(data_file, 'r') as f:
        intents = json.load(f)

    corpus = []
    tags = []

    for intent in intents:
        for pattern in intent['patterns']:
            corpus.append(clean_text(pattern))
            tags.append(intent['tag'])


    X_train, X_test, y_train, y_test = train_test_split(corpus, tags, test_size=0.2, random_state=42)

    print(f"Training set: {len(X_train)} samples")
    print(f"Testing set: {len(X_test)} samples")


    model = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])


    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)


    print("\n--- Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

if __name__ == "__main__":
    evaluate()
