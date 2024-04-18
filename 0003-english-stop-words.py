import nltk

nltk.download('stopwords')

en_stop_words = set(stopwords.words("english"))

print(en_stop_words)

"""
{'of', "she's", 'being', 'didn', 'as', 'into', 'from', 'more', 'below', 'our', 'have', 'o', 'both', 'in', 't', "hasn't", 'ours', 'against', 'their', 'were', 'doing', 'between', 'all', 'out', 'your', 'should', 'weren', 'they', 'too', 'by', 'd', "it's", "you've", 'why', 'further', 'only', "wasn't", 'couldn', 'after', 'himself', 'under', 'wouldn', 'few', 'itself', 'shouldn', 'can', 'if', 've', 'mustn', 'once', 'during', 'them', 'will', 'she', 'hasn', 'who', 'don', 'ma', 'again', 's', 'do', "don't", 'her', 'what', 'is', 'because', "didn't", 'me', 'does', 'aren', 'hadn', 'how', "isn't", 'ourselves', 'on', 'yourselves', 'he', 'through', 'you', 'just', 'yourself', 'that', 'some', 'i', 'about', 'its', 'while', 'm', "shouldn't", 'needn', "doesn't", "haven't", 'for', 'yours', 'and', 'there', 'we', 'nor', "won't", 'be', 'this', 'has', "weren't", 'which', 'such', 'a', "needn't", 'very', 'my', 'before', 'then', 'now', 'themselves', 'having', 'been', "should've", "couldn't", 'y', 'did', 'the', 'him', 'was', "you're", 'are', 'won', "wouldn't", 'these', 'most', 'than', 'theirs', 'an', 'own', 'other', 'down', "mightn't", 'hers', "mustn't", 'where', 'wasn', 'any', 'am', 'myself', 'not', "you'd", 'isn', 'with', 'no', 'herself', 'or', 'so', "aren't", 'above', "hadn't", 'mightn', 'll', 'shan', 'off', 'each', 'when', 'whom', 'doesn', 'haven', "you'll", 'those', 'over', 'but', "that'll", 'up', 'until', 'it', "shan't", 'his', 'at', 'to', 'here', 'ain', 'had', 're', 'same'}
"""
