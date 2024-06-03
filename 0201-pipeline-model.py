from transformers import pipeline

# ner -> named entity

# let's create our model

model_nlp_ner = pipeline("ner", model = "savasy/bert-base-turkish-ner-cased", tokenizer = "savasy/bert-base-turkish-ner-cased")
