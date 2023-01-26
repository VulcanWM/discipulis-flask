from flask import Flask, render_template
from vocab import nouns

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