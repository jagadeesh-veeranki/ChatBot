import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.nlp_utils import preprocess, stem, tokenize

class TestNLPUtils(unittest.TestCase):
    def test_tokenization(self):
        sentence = "Hello world!"
        tokens = tokenize(sentence)
        self.assertEqual(tokens, ['Hello', 'world', '!'])

    def test_stemming(self):
        word = "Running"
        self.assertEqual(stem(word), "run")
        self.assertEqual(stem("organization"), "organ")

    def test_preprocessing(self):
        # Stopwords removed? Punctuation gone? Lowercased? Stemmed?
        text = "The quick brown fox is running!"
        # 'the', 'is' are stopwords. '!' is punctuation.
        # expected: ['quick', 'brown', 'fox', 'run']
        tokens = preprocess(text)
        self.assertIn("quick", tokens)
        self.assertIn("fox", tokens)
        self.assertIn("run", tokens)
        self.assertNotIn("is", tokens)
        self.assertNotIn("!", tokens)

if __name__ == '__main__':
    unittest.main()
