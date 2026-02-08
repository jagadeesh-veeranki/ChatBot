import json
import pickle
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from src.utils.nlp_utils import preprocess 

# Custom tokenizer wrapper to use our NLTK stemmer in sklearn
def clean_text(text):
    # sklearn expects raw text string if we don't override tokenizer
    # Or we can pass our custom tokenizer:
    tokens = preprocess(text)
    return " ".join(tokens)  # Return space-joined tokens for CountVectorizer (simplest approach)

def train():
    print("Loading data...")
    data_file = os.path.join(os.path.dirname(__file__), '../../data/intents.json')
    with open(data_file, 'r') as f:
        intents = json.load(f)

    # Prepare training data
    corpus = []
    tags = []

    for intent in intents:
        for pattern in intent['patterns']:
            # We will use our preprocess function inside the pipeline or pre-process here
            # Let's preprocess here to have control
            clean_pattern = clean_text(pattern)
            corpus.append(clean_pattern)
            tags.append(intent['tag'])

    print(f"Training on {len(corpus)} sentences from {len(set(tags))} intents.")

    # Create Pipeline
    # 1. CountVectorizer: Convert text to matrix of token counts
    # 2. TfidfTransformer: Convert counts to frequencies (TF-IDF)
    # 3. MultinomialNB: Naive Bayes classifier suitable for word counts
    model = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])

    # Train
    model.fit(corpus, tags)
    print("Model trained successfully.")

    # Save Model
    model_path = os.path.join(os.path.dirname(__file__), '../../models/chatbot_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    # Save Intents/Tags mapping (optional, but good for response retrieval)
    # Actually, we need the FULL intent data to lookup responses by tag
    # Let's verify we can load intents.json in the bot class.
    
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train()
