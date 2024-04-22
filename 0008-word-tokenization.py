from nltk.tokenize import word_tokenize

sentence = "When he was young, his pocket was empty. A barking dog never bites. Go away!"

tokens = [word_tokenize(w) for w in sentence.split(".")]

print(tokens)

"""
[['When', 'he', 'was', 'young', ',', 'his', 'pocket', 'was', 'empty'], ['A', 'barking', 'dog', 'never', 'bites'], ['Go', 'away', '!']]

"""
