new_sentence = "A barking dog never bites and a rolling stone gathers no moss in ."

words = word_tokenize(new_sentence)

words = [w for w in words if w not in en_stop_words]

words = [w.lower() for w  in words if w.isalnum()]

print("Words: ", words)

"""
Words:  ['a', 'barking', 'dog', 'never', 'bites', 'rolling', 'stone', 'gathers', 'moss']
"""
