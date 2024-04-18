sentence = "A barking dog never bites and a rolling stone gathers no moss in 2024."

import re

pattern = r"[0-9]"

new_sentence = re.sub(pattern, '', sentence)

print(new_sentence)

"""
A barking dog never bites and a rolling stone gathers no moss in .
"""
