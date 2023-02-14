from flask import Flask, render_template, request, redirect, send_file
from vocab import nouns, verbs, noun_questions, verb_questions, metadata
from nouns import noun_english_to_latin, get_noun_table
from verbs import verb_english_to_latin, get_verb_table
from database import all_sets, get_set, add_set_play
from functions import generate_question, get_cookie, add_cookie
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()


@app.route("/")
def index():
    return render_template("index.html", metadata=metadata['index'])


@app.route("/robots.txt")
def robotstxt():
    return send_file("static/robots.txt")


@app.route("/all_nouns")
def all_nouns():
    nouns_dict = {}
    for noun in nouns.keys():
        latin_form = nouns[noun]
        nominative = latin_form.split(",")[0]
        clean = latin_form.replace(",", ", ")
        nouns_dict[noun] = {"Nominative": nominative, "Clean": clean}
    return render_template("all_nouns.html", nouns=nouns_dict, metadata=metadata['all_nouns'])


@app.route("/all_verbs")
def all_verbs():
    verbs_dict = {}
    for verb in verbs.keys():
        latin_form = verbs[verb]
        sing_1st = latin_form.split(",")[0]
        clean = latin_form.replace(",", ", ")
        verbs_dict[verb] = {"1stSingular": sing_1st, "Clean": clean}
    return render_template("all_verbs.html", verbs=verbs_dict, metadata=metadata['all_verbs'])


@app.route("/convert_noun")
def convert_noun_page():
    return render_template("convert_noun.html", metadata=metadata['convert_noun'])


@app.route("/convert_noun", methods=['POST', 'GET'])
def convert_noun_func():
    if request.method == 'POST':
        word = request.form['word']
        case = request.form['case']
        number = request.form['number']
        latin, nominative = noun_english_to_latin(word, case, number)
        if len(latin.split(" ")) != 1:
            return render_template("convert_noun.html", msg=latin, metadata=metadata['convert_noun'])
        return redirect(f"/noun/{nominative}?number={number}&case={case}")
    else:
        return redirect("/")


@app.route("/convert_verb")
def convert_verb_page():
    return render_template("convert_verb.html", metadata=metadata['convert_verb'])


@app.route("/convert_verb", methods=['POST', 'GET'])
def convert_verb_func():
    if request.method == 'POST':
        word = request.form['word']
        tense = request.form['tense']
        person = request.form['person']
        number = request.form['number']
        latin, nominative = verb_english_to_latin(word, person, number, tense)
        if len(latin.split(" ")) != 1:
            return render_template("convert_verb.html", msg=latin, metadata=metadata['convert_verb'])
        return redirect(f"/verb/{nominative}?tense={tense}&person={person}&number={number}")
    else:
        return redirect("/")


@app.route("/noun/<latin_word>")
def noun_page(latin_word):
    table, latin_form, word = get_noun_table(latin_word)
    if not table:
        return redirect("/")
    else:
        if request.args.get("number") is not None and request.args.get("case") is not None:
            the_id = request.args.get("number") + ":" + request.args.get("case")
        else:
            the_id = None
        site_metadata = {'Description': f"View the tables of number and case for the noun {latin_word} "
                                        f"(in english: {word})",
                         "Tags": ['noun', latin_word, word].extend(metadata['main']['Tags'])
                         }
        return render_template("noun.html", table=table, latin_form=latin_form, word=word, id=the_id,
                               number=request.args.get("number"), metadata=site_metadata)


@app.route("/verb/<latin_word>")
def verb_page(latin_word):
    table, latin_form, word = get_verb_table(latin_word)
    if not table:
        return redirect("/")
    else:
        if request.args.get("tense") is not None and request.args.get("person") is not None and request.args.get(
                "number") is not None:
            the_id = request.args.get("tense") + ":" + request.args.get("person") + " " + request.args.get("number")
        else:
            the_id = None
        site_metadata = {'Description': f"View the tables of tense, number and person for the verb {latin_word} "
                                        f"(in english: {word})",
                         "Tags": ['verb', latin_word, word].extend(metadata['main']['Tags'])
                         }
        return render_template("verb.html", table=table, latin_form=latin_form, word=word, id=the_id,
                               tense=request.args.get("tense"), metadata=site_metadata)


@app.route("/english_noun/<english_noun>")
def english_noun_redirect(english_noun):
    latin_word = noun_english_to_latin(english_noun, "nominative", "singular")[0]
    return redirect(f"/noun/{latin_word}")


@app.route("/english_verb/<english_verb>")
def english_verb_redirect(english_verb):
    latin_word = verb_english_to_latin(english_verb, "1st", "singular", "present")[0]
    return redirect(f"/verb/{latin_word}")


@app.route("/browse_sets")
def browse_sets():
    return render_template("browse_sets.html", sets=all_sets(), metadata=metadata['browse_sets'])


@app.route("/quiz/<quiz_id>")
def quiz_page(quiz_id):
    quiz_set = get_set(quiz_id)
    if not quiz_set:
        return redirect("/browse_sets")
    answer_type = request.args.get("answer_type")
    question_type = request.args.get("question_type")
    if not answer_type or not question_type:
        return redirect(f"/start_quiz/{quiz_id}")
    if not get_cookie(f"{quiz_id}:number") or (int(get_cookie(f"{quiz_id}:number")) > 10) \
            or not get_cookie(f"{quiz_id}:score"):
        add_cookie(f"{quiz_id}:number", "1")
        add_cookie(f"{quiz_id}:score", "0")
    score = get_cookie(f"{quiz_id}:score")
    number = get_cookie(f"{quiz_id}:number")
    question, choices, answers = generate_question(quiz_id, answer_type, question_type)
    add_cookie(f"{quiz_id}:answers", answers)
    post_url = f"/quiz/{quiz_id}?answer_type={answer_type}&question_type={question_type}"
    site_metadata = {'Description': f"See how you are doing in Latin by doing the set quiz for the set"
                                    f": {quiz_set['Name']}",
                     "Tags": [quiz_set['_id'], quiz_set['Type'], 'quiz', 'set'].extend(metadata['main']['Tags'])
                     }
    return render_template("quiz_question.html", score=score, number=number, question=question,
                           choices=choices, quiz_set=quiz_set, post_url=post_url,
                           quiz_ended=False, metadata=site_metadata)


@app.route("/quiz/<quiz_id>", methods=['POST', 'GET'])
def quiz_answer(quiz_id):
    quiz_set = get_set(quiz_id)
    if not quiz_set:
        return redirect("/browse_sets")
    if not get_cookie(f"{quiz_id}:number") or not get_cookie(f"{quiz_id}:score") \
            or not get_cookie(f"{quiz_id}:answers"):
        return redirect(f"/start_quiz/{quiz_id}")
    answer_type = request.args.get("answer_type")
    question_type = request.args.get("question_type")
    if not answer_type or not question_type:
        return redirect(f"/start_quiz/{quiz_id}")
    answers = get_cookie(f"{quiz_id}:answers")
    answer = request.form['answer'].lower()
    if answer in answers.split(","):
        score = int(get_cookie(f"{quiz_id}:score")) + 1
        add_cookie(f"{quiz_id}:score", str(score))
    number = int(get_cookie(f"{quiz_id}:number"))
    if number == 10:
        add_set_play(quiz_id)
        add_cookie(f"{quiz_id}:number", False)
        same_url = f"/quiz/{quiz_id}?answer_type={answer_type}&question_type={question_type}"
        score = get_cookie(f'{quiz_id}:score')
        site_metadata = {'Description': f"See how you are doing in Latin by doing the set quiz for the set"
                                        f": {quiz_set['Name']}",
                         "Tags": [quiz_set['_id'], quiz_set['Type'], 'quiz', 'set'].extend(metadata['main']['Tags'])
                         }
        return render_template("quiz_question.html", quiz_ended=True, score=score, same_url=same_url, quiz_set=quiz_set,
                               metadata=site_metadata)
    else:
        add_cookie(f"{quiz_id}:number", number + 1)
        return redirect(f"/quiz/{quiz_id}?answer_type={answer_type}&question_type={question_type}")


@app.route("/start_quiz/<quiz_id>")
def start_quiz_page(quiz_id):
    quiz_set = get_set(quiz_id)
    if not quiz_set:
        return redirect("/browse_sets")
    questions = {}
    if 'noun' in quiz_set['Type']:
        questions.update(noun_questions)
    if 'verb' in quiz_set['Type']:
        questions.update(verb_questions)
    site_metadata = {'Description': f"Start the quiz for set: {quiz_set['Name']} by filling in the quiz settings",
                     "Tags": [quiz_set['_id'], quiz_set['Type'], 'quiz', 'set'].extend(metadata['main']['Tags'])
                     }
    return render_template("quiz_start.html", quiz=quiz_set, questions=questions, metadata=site_metadata)


@app.route("/start_quiz/<quiz_id>", methods=['POST', 'GET'])
def start_quiz_func(quiz_id):
    quiz_set = get_set(quiz_id)
    if not quiz_set:
        return redirect("/browse_sets")
    answer_type = request.form['answer_type']
    question_type = ""
    for request_id in request.form:
        if request_id.startswith('question_'):
            question_id = request_id.replace("question_", "")
            question_type += question_id
    if question_type == "":
        return redirect(f"/start_quiz/{quiz_id}")
    return redirect(f"/quiz/{quiz_id}?answer_type={answer_type}&question_type={question_type}")


@app.route("/set/<set_id>")
def view_set(set_id):
    quiz_set = get_set(set_id)
    if not quiz_set:
        return redirect("/browse_sets")
    contains = quiz_set['Type'].split("-")
    contains = [s + "s" for s in contains]
    contains = "".join(contains)
    quiz_set['Contains'] = contains
    site_metadata = {'Description': f"See what the set: {quiz_set['Name']} contains and what vocabulary it has",
                     "Tags": [quiz_set['_id'], quiz_set['Type'], 'quiz', 'set'].extend(metadata['main']['Tags'])
                     }
    return render_template("view_set.html", quiz_set=quiz_set, metadata=site_metadata)
