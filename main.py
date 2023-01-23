from nouns import noun_english_to_latin
from verbs import verb_english_to_latin
from vocab import nouns, verbs

for noun in nouns.keys():
    print(f"{noun}: dative and singular")
    print(noun_english_to_latin(noun, "dative", "singular"))


print(verb_english_to_latin("rule", "2nd", "plural", "present"))
print(verb_english_to_latin("rule", "2nd", "plural", "future"))
print(verb_english_to_latin("rule", "2nd", "plural", "perfect"))
print(verb_english_to_latin("hear", "2nd", "plural", "present"))
print(verb_english_to_latin("hear", "2nd", "plural", "future"))
print(verb_english_to_latin("hear", "2nd", "plural", "perfect"))