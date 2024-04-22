from nltk import sent_tokenize
import nltk
nltk.download('punkt')

sentences = [
    "A rolling stone gathers no moss...",
    "Winter is coming",
    "Out of sight, out of mind!"
]

tokens = [sent_tokenize(s) for s in sentences]

print(tokens)

"""
[['A rolling stone gathers no moss...'], ['Winter is coming'], ['Out of sight, out of mind!']]
"""
