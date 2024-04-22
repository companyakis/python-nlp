nltk.download('averaged_perceptron_tagger')

tokens = [['When', 'he', 'was', 'young', ',', 'his', 'pocket', 'was', 'empty'], ['A', 'barking', 'dog', 'never', 'bites'], ['Go', 'away', '!']]

#pos => parts of speech tagging

token_pos_tagging = [(token, nltk.pos_tag(token)) for token in tokens]

print(token_pos_tagging)

"""
[(['When', 'he', 'was', 'young', ',', 'his', 'pocket', 'was', 'empty'], [('When', 'WRB'), ('he', 'PRP'), ('was', 'VBD'), ('young', 'JJ'), (',', ','), ('his', 'PRP$'), ('pocket', 'NN'), ('was', 'VBD'), ('empty', 'JJ')]), (['A', 'barking', 'dog', 'never', 'bites'], [('A', 'DT'), ('barking', 'NN'), ('dog', 'NN'), ('never', 'RB'), ('bites', 'NNS')]), (['Go', 'away', '!'], [('Go', 'VB'), ('away', 'RP'), ('!', '.')])]

"""
