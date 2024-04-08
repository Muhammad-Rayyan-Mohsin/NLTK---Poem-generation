from nltk.util import ngrams
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import random

file_path = "william shakespeare.txt" 
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # 2. Read the file content
        shakespeare = file.read()

        # 3. Output the text
        # print("File content:")
        # print(file_content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


file_path2 = "Robert Frost.txt"  
try:
    with open(file_path2, 'r', encoding='utf-8') as file:
        # 2. Read the file content
        robert = file.read()

        # 3. Output the text
        # print("File content:")
        # print(file_content)
except FileNotFoundError:
    print(f"File '{file_path2}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

robert = robert.lower()
shakespeare = shakespeare.lower()

robert_tokens = word_tokenize(robert)
shakespeare_tokens = word_tokenize(shakespeare)

##----------------------------------------------------------Robert N-grams-------------------------##

robert_unigrams = list(ngrams(robert_tokens,1))
robert_unigramFD = nltk.FreqDist(robert_unigrams)

robert_bigrams = list(ngrams(robert_tokens, 2))
robert_bigramsFD = nltk.FreqDist(robert_bigrams)

robert_trigrams = list(ngrams(robert_tokens,3))
robert_trigramFD = nltk.FreqDist(robert_trigrams)

##----------------------------------------------------------Shakespeare N-grams-------------------------##

shakespeare_unigrams = list(ngrams(shakespeare_tokens,1))
shakespeare_unigramFD = nltk.FreqDist(shakespeare_unigrams)

shakespeare_bigrams = list(ngrams(shakespeare_tokens,2))
shakespeare_bigramFD = nltk.FreqDist(shakespeare_bigrams)

shakespeare_trigrams = list(ngrams(shakespeare_tokens,3))
shakespeare_trigramFD = nltk.FreqDist(shakespeare_trigrams)


##----------------------------------------------------------Shakespeare N-grams-------------------------##

# ngrams = {}

# for word in robert_unigramFD:
#     words = [word for word in robert_unigramFD if word[0].isalpha()]
#     for ix in range(len(words)-1):
#         try:
#             ngrams[words[ix]].append(words[ix+1])
#         except KeyError as _:
#             ngrams[words[ix]] = []
#             ngrams[words[ix]].append(words[ix+1])

# import random

# def generate_text(n = 7):
#     words = []
#     next_word = random.choice(list(ngrams.keys()))
#     words.append(next_word)
#     while len(words) < n:
#         next_word = random.choice(ngrams[next_word])
#         words.append(next_word)

#     return ' '.join(words)  

# generate_text()

def generate_verse(model_unigramFD, model_bigramFD, model_trigramFD, starting_word, verse_length):
    verse = [starting_word]
    current_word = starting_word

    for _ in range(verse_length - 1):
        # Choose the next word based on the models
        next_word_options = []

        # Unigram model
        next_word_options.extend([word[0] for word in model_unigramFD if word[0] == current_word])

        # Bigram model
        bigram_options = [word[1] for word in model_bigramFD if word[0] == current_word]
        next_word_options.extend(bigram_options)

        # Trigram model
        trigram_options = [word[2] for word in model_trigramFD if word[0] == current_word]
        next_word_options.extend(trigram_options)

        # Choose a random next word
        next_word = random.choice(next_word_options)
        verse.append(next_word)
        current_word = next_word

    return ' '.join(verse)


# Generate a random number in the range [7...10]
verse_length = random.randint(7, 10)

# Select the first word for each poet
starting_word_robert = random.choice(robert_tokens)
starting_word_shakespeare = random.choice(shakespeare_tokens)

# Generate verses
robert_verse1 = generate_verse(robert_unigramFD, robert_bigramsFD, robert_trigramFD, starting_word_robert, verse_length)
shakespeare_verse1 = generate_verse(shakespeare_unigramFD, shakespeare_bigramFD, shakespeare_trigramFD, starting_word_shakespeare, verse_length)

robert_verse2 = generate_verse(robert_unigramFD, robert_bigramsFD, robert_trigramFD, starting_word_robert, verse_length)
shakespeare_verse2 = generate_verse(shakespeare_unigramFD, shakespeare_bigramFD, shakespeare_trigramFD, starting_word_shakespeare, verse_length)

robert_verse3 = generate_verse(robert_unigramFD, robert_bigramsFD, robert_trigramFD, starting_word_robert, verse_length)
shakespeare_verse3 = generate_verse(shakespeare_unigramFD, shakespeare_bigramFD, shakespeare_trigramFD, starting_word_shakespeare, verse_length)

robert_verse4 = generate_verse(robert_unigramFD, robert_bigramsFD, robert_trigramFD, starting_word_robert, verse_length)
shakespeare_verse4 = generate_verse(shakespeare_unigramFD, shakespeare_bigramFD, shakespeare_trigramFD, starting_word_shakespeare, verse_length)

# Print the verses
print("Robert Frost's Verses:")
print(robert_verse1)
print(robert_verse2)
print(robert_verse3)
print(robert_verse4)

print("\nShakespeare's Verse:")
print(shakespeare_verse1)
print(shakespeare_verse2)
print(shakespeare_verse3)
print(shakespeare_verse4)
print("\n")  # Print an empty line after the stanza



