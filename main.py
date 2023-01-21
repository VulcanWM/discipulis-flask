from nouns import noun_english_to_latin
from vocab import nouns

for noun in nouns.keys():
    print(noun)
    print(noun_english_to_latin(noun, "dative", "singular"))
