import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

# Download NLTK resources (first run only)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')



try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def preprocess(sentence):
    tokens = tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    clean_tokens = [
        stem(w) for w in tokens 
        if w not in string.punctuation and w.lower() not in stop_words
    ]
    return clean_tokens
