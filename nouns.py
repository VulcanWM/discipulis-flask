from vocab import nouns

cases = ['nominative', 'vocative', 'accusative', 'genetive', 'dative', 'ablative']
numbers = ['singular', 'plural']

first_declension = ["a","a","am","ae","ae","a","ae","ae","as","arum","is","is"]

def noun_english_to_latin(word, case, number):
    if case not in cases:
        return "This is not a case"
    if number not in numbers:
        return "A number has to be singular or plural"
    if word not in nouns.keys():
        return "This word is not in the word list"
    index = cases.index(case)
    if number == "plural":
        index += 6
    latin_form = nouns[word]
    nominative = latin_form.split(",")[0]
    genetive = latin_form.split(",")[1]
    if genetive.endswith("ae"):
        latin_word = nominative[:-1] + first_declension[index]
    return latin_word
