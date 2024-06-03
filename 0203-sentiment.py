from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

sentiment_model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")

sa_tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")

sentiment_pipeline = pipeline("sentiment-analysis", tokenizer = sa_tokenizer, model = sentiment_model)

sentence = "Hava çok güzel, ama içimde bir sıkıntı var. Bu güzel havalar da beni mutlu edemedi!"

sentiment_result = sentiment_pipeline(sentence)

print(sentiment_result)

"""
[{'label': 'negative', 'score': 0.9986836314201355}]
"""
