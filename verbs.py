from vocab import verbs, numbers, persons, tenses

first_conjugation = {
    'present': ['o', 'as', 'at', 'amus', 'atis', 'ant'],
    'imperfect': ['abam', 'abas', 'abat', 'abamus', 'abatis', 'abant'],
    'perfect': ['vi', 'visti', 'vit', 'vimus', 'vistis', 'verunt'],
    'future': ['abo', 'abis', 'abit', 'abimus', 'abitis', 'abunt']
}


def verb_english_to_latin(word, person, number, tense):
    if tense not in tenses:
        return "This is not a case"
    if number not in numbers:
        return "A number has to be singular or plural"
    if word not in verbs.keys():
        return "This word is not in the word list"
    if person not in persons:
        return "The person has to be 1st, 2nd or 3rd"
    latin_form = verbs[word]
    infinitive = latin_form.split(",")[1]
    perfect = latin_form.split(",")[2]
    index = persons.index(person)
    if number == "plural":
        index += 3
    if infinitive.endswith("are"):
        # 1st conjugation
        if tense != "perfect":
            latin_word = infinitive[:-3] + first_conjugation[tense][index]
        else:
            latin_word = perfect[:-2] + first_conjugation['perfect'][index]
    return latin_word

