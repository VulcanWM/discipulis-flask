from vocab import nouns, numbers, cases

first_declension = \
    ["a", "a", "am", "ae", "ae", "a", "ae", "ae", "as", "arum", "is", "is"]
second_declension_masc = \
    ['us', 'e', 'um', 'i', 'o', 'o', 'i', 'i', 'os', 'orum', 'is', 'is']
second_declension_masc_er = \
    ['', '', 'um', 'i', 'o', 'o', 'i', 'i', 'os', 'orum', 'is', 'is']
second_declension_neut = \
    ['um', 'um', 'um', 'i', 'o', 'o', 'a', 'a', 'a', 'orum', 'is', 'is']
second_declension_irregular = \
    {
       'filius': ['filius', 'fili', 'filium', 'fili', 'filio/filii', 'filio', 'filio',
                  'filii', 'filii', 'filios', 'filiorum', 'filiis', 'filiis'],
       'deus': ['deus', 'deus', 'deum', 'dei', 'deo', 'deo',
                'di/dei', 'di/dei', 'deos', 'deorum/deum', 'dis/deis', 'dis/deis'],
       'vir': ['vir', 'vir', 'virum', 'viri', 'viro', 'viro',
               'viri', 'viri', 'viros', 'virorum/virum', 'viris', 'viris']
    }
fourth_declension_masc = \
    ['us', 'us', 'um', 'us', 'ui', 'u', 'us', 'us', 'us', 'uum', 'ibus', 'ibus']
fourth_declension_neut = \
    ['u', 'u', 'u', 'us', 'u', 'u', 'ua', 'ua', 'ua', 'uum', 'ibus', 'ibus']
fourth_declension_irregular = \
    {
        "domus": ['domus', 'domus', 'domum', 'domus', 'domui/domo', 'domo',
                  "domus", "domus", "domos/domus", "domuum/domorum", "domibus", "domibus"]
    }
non_increasing_third_declension = ['civis', 'cubile']
third_declension_normal = \
    ['', '', 'em', 'is', 'i', 'e', 'es', 'es', 'es', 'um', 'ibus', 'ibus']
third_declension_neut = \
    ['', '', '', 'is', 'i', 'e', 'a', 'a', 'a', 'um', 'ibus', 'ibus']
third_declension_non_normal = \
    ['', '', 'em', 'is', 'i', 'e', 'es', 'es', 'es', 'ium', 'ibus', 'ibus']
third_declension_non_neut = \
    ['', '', '', 'is', 'i', 'i', 'ia', 'ia', 'ia', 'ium', 'ibus', 'ibus']
fifth_declension = \
    ['es', 'es', 'em', 'ei', 'ei', 'e', 'es', 'es', 'es', 'erum', 'ebus', 'ebus']


def noun_english_to_latin(word, case, number):
    if case not in cases:
        return "<p class='red'>This is not a case</p>", False
    if number not in numbers:
        return "<p class='red'>A number has to be singular or plural</p>", False
    if word not in nouns.keys():
        return f"<p class='red'>{word} is not in the word list</p>", False
    index = cases.index(case)
    if number == "plural":
        index += 6
    latin_form = nouns[word]
    nominative = latin_form.split(",")[0]
    genitive = latin_form.split(",")[1]
    gender = latin_form.split(",")[2]
    declension = latin_form.split(",")[3]
    if declension == "1st":
        # 1st declension
        latin_word = nominative[:-1] + first_declension[index]
    if declension == "2nd":
        # 2nd declension
        if nominative in second_declension_irregular.keys():
            # 2nd declension irregular
            latin_word = second_declension_irregular[nominative][index]
        else:
            # not irregular
            if nominative.endswith("us"):
                # 2nd declension masculine normal
                latin_word = nominative[:-2] + second_declension_masc[index]
            if nominative.endswith("um"):
                # 2nd declension neuter
                latin_word = nominative[:-2] + second_declension_neut[index]
            if nominative.endswith("er"):
                # 2nd declension masculine other
                latin_word = nominative + second_declension_masc_er[index]
    if declension == "3rd":
        # 3rd declension noun
        if nominative in non_increasing_third_declension:
            # Non-increasing 3rd declension
            if gender == "n.":
                # Neuter non-increasing 3rd declension
                if index in [0, 1, 2]:
                    latin_word = nominative
                else:
                    latin_word = genitive[:-2] + third_declension_non_neut[index]
            else:
                # Masc/Fem non-increasing 3rd declension
                if index in [0, 1]:
                    latin_word = nominative
                else:
                    latin_word = genitive[:-2] + third_declension_non_normal[index]
        else:
            # Increasing 3rd declension
            if gender == "n.":
                # Neuter increasing 3rd declension
                if index in [0, 1, 2]:
                    latin_word = nominative
                else:
                    latin_word = genitive[:-2] + third_declension_neut[index]
            else:
                # Masc/Fem increasing 3rd declension
                if index in [0, 1]:
                    latin_word = nominative
                else:
                    latin_word = genitive[:-2] + third_declension_normal[index]
    if declension == "4th":
        # 4th declension
        if nominative in fourth_declension_irregular.keys():
            # 4th declension irregular
            latin_word = fourth_declension_irregular[nominative][index]
        else:
            # not irregular
            if nominative.endswith("us"):
                # 2nd declension masculine
                latin_word = nominative[:-2] + fourth_declension_masc[index]
            if nominative.endswith("u"):
                # 2nd declension neuter
                latin_word = nominative[:-1] + fourth_declension_neut[index]
    if declension == "5th":
        # 5th declension
        latin_word = genitive[:-2] + fifth_declension[index]
    return latin_word, nominative


def get_noun_table(nominative):
    word = None
    key_list = list(nouns.keys())
    val_list = list(nouns.values())
    latin_form = None
    for form in val_list:
        if form.startswith(nominative):
            position = val_list.index(form)
            word = key_list[position]
            latin_form = form
    if word is None:
        return False, False, False
    table = {"singular": {}, "plural": {}}
    for number in list(table.keys()):
        for case in cases:
            table[number][case] = noun_english_to_latin(word, case, number)[0]
    return table, latin_form, word


