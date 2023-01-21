from vocab import nouns, numbers, cases

first_declension = ["a", "a", "am", "ae", "ae", "a", "ae", "ae", "as", "arum", "is", "is"]
second_declension_masc = ['us', 'e', 'um', 'i', 'o', 'o', 'i', 'i', 'os', 'orum', 'is', 'is']
second_declension_masc_er = ['', '', 'um', 'i', 'o', 'o', 'i', 'i', 'os', 'orum', 'is', 'is']
second_declension_neut = ['um', 'um', 'um', 'i', 'o', 'o', 'a', 'a', 'a', 'orum', 'is', 'is']
second_declension_irregular = \
    {
       'filius': ['filius', 'fili', 'filium', 'fili', 'filio/filii', 'filio', 'filio',
                  'filii', 'filii', 'filios', 'filiorum', 'filiis', 'filiis'],
       'deus': ['deus', 'deus', 'deum', 'dei', 'deo', 'deo'
                'di/dei', 'di/dei', 'deos', 'deorum/deum', 'dis/deis', 'dis/deis'],
       'vir': ['vir', 'vir', 'virum', 'viri', 'viro', 'viro',
               'viri', 'viri', 'viros', 'virorum/virum', 'viris', 'viris']
    }
fourth_declension_masc = ['us', 'us', 'um', 'us', 'ui', 'u', 'us', 'us', 'us', 'uum', 'ibus', 'ibus']
fourth_declension_neut = ['u', 'u', 'u', 'us', 'u', 'u', 'ua', 'ua', 'ua', 'uum', 'ibus', 'ibus']
fourth_declension_irregular = \
    {
        "domus": ['domus', 'domus', 'domum', 'domus', 'domui/domo', 'domo',
                  "domus", "domus", "domos/domus", "domuum/domorum", "domibus", "domibus"]
    }


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
    genitive = latin_form.split(",")[1]
    if genitive.endswith("ae"):
        # 1st declension
        latin_word = nominative[:-1] + first_declension[index]
    if genitive.endswith("i"):
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
    if genitive.endswith("us"):
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
    return latin_word
