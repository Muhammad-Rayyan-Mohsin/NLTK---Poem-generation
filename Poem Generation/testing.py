from nltk.util import ngrams
import nltk
import random
from nltk.tokenize import word_tokenize, sent_tokenize

import string

# Sample text with punctuation
text = "Hello, World! This is an example text with punctuations."

# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from the text
text_without_punctuation = text.translate(translator)

print(text_without_punctuation)
