from flask import Flask, render_template, request, redirect, send_file
from vocab import nouns, verbs
from nouns import noun_english_to_latin
from verbs import verb_english_to_latin

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/all_nouns")
def all_nouns():
    nouns_dict = {}
    for noun in nouns.keys():
        latin_form = nouns[noun]
        nominative = latin_form.split(",")[0]
        clean = latin_form.replace(",", ", ")
        nouns_dict[noun] = {"Nominative": nominative, "Clean": clean}
    return render_template("all_nouns.html", nouns=nouns_dict)


@app.route("/all_verbs")
def all_verbs():
    verbs_dict = {}
    for verb in verbs.keys():
        latin_form = verbs[verb]
        sing_1st = latin_form.split(",")[0]
        clean = latin_form.replace(",", ", ")
        verbs_dict[verb] = {"1stSingular": sing_1st, "Clean": clean}
    return render_template("all_verbs.html", verbs=verbs_dict)


@app.route("/convert_noun")
def convert_noun_page():
    return render_template("convert_noun.html")


@app.route("/convert_noun", methods=['POST', 'GET'])
def convert_noun_func():
    if request.method == 'POST':
        word = request.form['word']
        case = request.form['case']
        number = request.form['number']
        latin = noun_english_to_latin(word, case, number)
        msg = f"<p>The {number} {case} of {word} is <strong>{latin}</strong></p>"
        return render_template("convert_noun.html", msg=msg)
    else:
        return redirect("/")


@app.route("/convert_verb")
def convert_verb_page():
    return render_template("convert_verb.html")


@app.route("/convert_verb", methods=['POST', 'GET'])
def convert_verb_func():
    if request.method == 'POST':
        word = request.form['word']
        tense = request.form['tense']
        person = request.form['person']
        number = request.form['number']
        latin = verb_english_to_latin(word, person, number, tense)
        msg = f"<p>The {tense} {person} person {number} of {word} is <strong>{latin}</strong></p>"
        return render_template("convert_verb.html", msg=msg)
    else:
        return redirect("/")
