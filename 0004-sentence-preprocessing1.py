nltk.download('punkt')

sentence = "A barking dog never bites and a rolling stone gathers no moss in 2024."

#tokenization

words = word_tokenize(sentence)

#let's use list comprehension

words = [w for w in words if w not in en_stop_words]

print("Step 1 words: ", words)

words = [w.lower() for w  in words if w.isalnum()]

print("Step 2 words: ", words)

"""
Step 1 words:  ['A', 'barking', 'dog', 'never', 'bites', 'rolling', 'stone', 'gathers', 'moss', '2024', '.']

Step 2 words:  ['a', 'barking', 'dog', 'never', 'bites', 'rolling', 'stone', 'gathers', 'moss', '2024']
"""
