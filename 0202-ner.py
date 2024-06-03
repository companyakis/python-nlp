sample_text = "Bilge Kağan döneminde, Türkler Çin'e karşı güçlüydü. Bugün ise Doğu Türkistan'da Çin tarafından Türklere karşı soykırım yapılmaktadır."

text_ners = model_nlp_ner(sample_text)

print(text_ners)

"""
[{'entity': 'B-PER', 'score': 0.99906904, 'index': 1, 'word': 'Bilge', 'start': 0, 'end': 5}, 
{'entity': 'I-PER', 'score': 0.99869007, 'index': 2, 'word': 'Ka', 'start': 6, 'end': 8}, 
{'entity': 'I-PER', 'score': 0.997593, 'index': 3, 'word': '##ğan', 'start': 8, 'end': 11}, 
{'entity': 'B-LOC', 'score': 0.97091717, 'index': 7, 'word': 'Çin', 'start': 31, 'end': 34}, 
{'entity': 'B-LOC', 'score': 0.96133906, 'index': 17, 'word': 'Doğu', 'start': 63, 'end': 67}, 
{'entity': 'I-LOC', 'score': 0.99258065, 'index': 18, 'word': 'Türkistan', 'start': 68, 'end': 77}, 
{'entity': 'B-LOC', 'score': 0.883813, 'index': 21, 'word': 'Çin', 'start': 81, 'end': 84}]
"""
