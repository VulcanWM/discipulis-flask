from vocab import verbs, numbers, persons, tenses, perfect_stems, verb_types

first_conjugation = {
    'present': ['o', 'as', 'at', 'amus', 'atis', 'ant'],
    'imperfect': ['abam', 'abas', 'abat', 'abamus', 'abatis', 'abant'],
    'perfect': ['i', 'isti', 'it', 'imus', 'istis', 'erunt'],
    'future': ['abo', 'abis', 'abit', 'abimus', 'abitis', 'abunt'],
    'future perfect': ['ero', 'eris', 'erit', 'erimus', 'eritis', 'erint'],
    'pluperfect': ['eram', 'eras', 'erat', 'eramus', 'eratis', 'erant']
}

second_conjugation = {
    'present': ['o', 'es', 'et', 'emus', 'etis', 'ent'],
    'imperfect': ['ebam', 'ebas', 'ebat', 'ebamus', 'ebatis', 'ebant'],
    'perfect': ['i', 'isti', 'it', 'imus', 'istis', 'erunt'],
    'future': ['ebo', 'ebis', 'ebit', 'ebimus', 'ebitis', 'ebunt'],
    'future perfect': ['ero', 'eris', 'erit', 'erimus', 'eritis', 'erint'],
    'pluperfect': ['eram', 'eras', 'erat', 'eramus', 'eratis', 'erant']
}

third_conjugation = {
    'present': ['o', 'is', 'it', 'imus', 'itis', 'unt'],
    'imperfect': ['ebam', 'ebas', 'ebat', 'ebamus', 'ebatis', 'ebant'],
    'perfect': ['i', 'isti', 'it', 'imus', 'istis', 'erunt'],
    'future': ['am', 'es', 'et', 'emus', 'etis', 'ent'],
    'future perfect': ['ero', 'eris', 'erit', 'erimus', 'eritis', 'erint'],
    'pluperfect': ['eram', 'eras', 'erat', 'eramus', 'eratis', 'erant']
}


def verb_english_to_latin(word, person, number, tense):
    if tense not in tenses:
        return "<p class='red'>This is not a case</p>", False
    if number not in numbers:
        return "<p class='red'>A number has to be singular or plural</p>", False
    if word not in verbs.keys():
        return f"<p class='red'>{word} is not in the word list</p>", False
    if person not in persons:
        return "<p class='red'>The person has to be 1st, 2nd or 3rd</p>", False
    latin_form = verbs[word]
    nominative = latin_form.split(",")[0]
    infinitive = latin_form.split(",")[1]
    perfect = latin_form.split(",")[2]
    conjugation = latin_form.split(",")[-1]
    index = persons.index(person)
    if number == "singular" and person == "1st" and tense == "present":
        return nominative, nominative
    if number == "plural":
        index += 3
    if conjugation == "1st":
        # 1st conjugation
        if tense not in perfect_stems:
            latin_word = infinitive[:-3] + first_conjugation[tense][index]
        else:
            latin_word = perfect[:-1] + first_conjugation[tense][index]
    if conjugation == "2nd":
        # 2nd conjugation
        if tense not in perfect_stems:
            latin_word = infinitive[:-3] + second_conjugation[tense][index]
        else:
            latin_word = perfect[:-1] + second_conjugation[tense][index]
    if conjugation == "3rd":
        # 3rd conjugation
        if tense not in perfect_stems:
            latin_word = infinitive[:-3] + third_conjugation[tense][index]
        else:
            latin_word = perfect[:-1] + third_conjugation[tense][index]
    if conjugation == "4th":
        # 4th conjugation
        if tense in perfect_stems:
            latin_word = perfect[:-1] + third_conjugation[tense][index]
        elif tense == "present":
            latin_word = infinitive[:-3] + third_conjugation[tense][index]
        else:
            latin_word = infinitive[:-2] + third_conjugation[tense][index]
    if conjugation == "mixed":
        # mixed conjugation
        if tense in perfect_stems:
            latin_word = perfect[:-1] + third_conjugation[tense][index]
        elif tense == "present":
            latin_word = infinitive[:-3] + third_conjugation[tense][index]
        else:
            latin_word = nominative[:-1] + third_conjugation[tense][index]
    return latin_word, nominative


def get_verb_table(first_sing):
    word = None
    key_list = list(verbs.keys())
    val_list = list(verbs.values())
    latin_form = None
    for form in val_list:
        if form.split(",")[0] == first_sing:
            position = val_list.index(form)
            word = key_list[position]
            latin_form = form
    if word is None:
        return False, False, False
    table = {"present": {},
             "future": {},
             "imperfect": {},
             "perfect": {},
             "pluperfect": {},
             "future perfect": {}}
    for tense in list(table.keys()):
        for type in verb_types:
            person = type.split(" ")[0]
            number = type.split(" ")[1]
            table[tense][type] = verb_english_to_latin(word, person, number, tense)[0]
    return table, latin_form, word
