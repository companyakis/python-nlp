nltk.download('wordnet')

words = ['a', 'barking', 'dog', 'never', 'bites', 'rolling', 'stone', 'gathers', 'moss']

wordnet_lemmatizer = WordNetLemmatizer()

lemmatized_words = [wordnet_lemmatizer.lemmatize(w) for w in words]

print(lemmatized_words)

"""
['a', 'barking', 'dog', 'never', 'bite', 'rolling', 'stone', 'gather', 'moss']
"""
