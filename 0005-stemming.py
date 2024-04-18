words = ['a', 'barking', 'dog', 'never', 'bites', 'rolling', 'stone', 'gathers', 'moss']

porter_stemmer = PorterStemmer()

stemmed_words = [porter_stemmer.stem(w) for w in words]

print(stemmed_words)

"""
['a', 'bark', 'dog', 'never', 'bite', 'roll', 'stone', 'gather', 'moss']

"""
