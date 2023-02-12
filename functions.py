from flask import session
from database import get_set
import random
from vocab import main_questions, verb_questions, noun_questions, all_questions, cases, tenses, verb_types
from nouns import get_noun_table, noun_english_to_latin
from verbs import get_verb_table, verb_english_to_latin


def add_cookie(key, value):
    session[key] = value


def del_cookies():
    session.clear()


def get_cookie(key):
    if x := session.get(key):
        return x
    else:
        return False


def generate_question(quiz_id, answer_type, question_type):
    quiz_set = get_set(quiz_id)
    if not quiz_set:
        return False
    if answer_type == "both":
        this_a_type = random.choice(["written", "multiple"])
    else:
        this_a_type = answer_type
    question_word = random.choice(list(quiz_set['Words'].keys()))
    question_word_type = quiz_set['Words'][question_word]
    word_question_type_list = []
    for char in question_type:
        if char in main_questions.keys():
            word_question_type_list.append(char)
        else:
            if question_word_type == "noun":
                if char in noun_questions.keys():
                    word_question_type_list.append(char)
            if question_word_type == "verb":
                if char in verb_questions.keys():
                    word_question_type_list.append(char)
    this_q_type_index = random.randint(0, len(word_question_type_list)-1)
    this_q_type_char = word_question_type_list[this_q_type_index]
    this_q_type = all_questions[this_q_type_char]
    if this_q_type == "Cases":
        question_case = random.choice(cases)
        number = random.choice(['singular', 'plural'])
        nominative = noun_english_to_latin(question_word, "nominative", "singular")[0]
        word_table = get_noun_table(nominative)[0]
        latin_word = word_table[number][question_case]
        question = f"{latin_word} is {number}. What case is it?"
        answers = []
        for loop_case in word_table[number].keys():
            if word_table[number][loop_case] == latin_word:
                answers.append(loop_case)
        answers = ",".join(answers)
        if this_a_type == "written":
            choices = "input"
        else:
            question_cases = ['nominative', 'vocative', 'accusative', 'genitive', 'dative', 'ablative']
            choices = [question_case]
            question_cases.remove(question_case)
            for i in range(3):
                option_case = random.choice(question_cases)
                choices.append(option_case)
                question_cases.remove(option_case)
        return question, choices, answers
    if this_q_type == "Tenses":
        tense = random.choice(tenses)
        present_singular = verb_english_to_latin(question_word, "1st", "singular", "present")[0]
        word_table = get_verb_table(present_singular)[0]
        word_verb_type = random.choice(verb_types)
        latin_word = word_table[tense][word_verb_type]
        question = f"What tense is {latin_word}?"
        if this_a_type == "written":
            choices = "input"
        else:
            question_tenses = ['present', 'imperfect', 'perfect', 'future', 'pluperfect', 'future perfect']
            choices = [tense]
            question_tenses.remove(tense)
            for i in range(3):
                option_tense = random.choice(question_tenses)
                choices.append(option_tense)
                question_tenses.remove(option_tense)
        return question, choices, tense
    if this_q_type == "English to Latin":
        pass
    if this_q_type == "Latin to English":
        pass
    return False

