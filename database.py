import pymongo
import datetime

clientm = pymongo.MongoClient("mongodb+srv://Hello:There@discipulis.kbuwme3.mongodb.net/?retryWrites=true&w=majority")
quizdb = clientm.Quiz
setscol = quizdb.Sets


def all_sets():
    sets = []
    for set in setscol.find():
        sets.append(set)
    return sets


def add_set(set_id, set_name, set_type, set_creator, set_words):
    # set name will be 'noun' if just nouns, 'noun-verb' if nouns and verbs
    # set_words will be a dict in format {"english word": "type"}
    # example: set_words = {"love": "verb", "girl": "noun"}, set_type = "noun-verb"
    current_date = datetime.datetime.now()
    current_date = current_date. \
        replace(tzinfo=datetime.timezone.utc)
    current_date = current_date.isoformat()
    document = [{
        "_id": set_id,
        "Name": set_name,
        "Type": set_type,
        "Creator": set_creator,
        "Words": set_words,
        "Plays": 0,
        "Favourites": 0,
        "Created": current_date,
    }]
    setscol.insert_many(document)
