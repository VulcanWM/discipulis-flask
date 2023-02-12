import pymongo
import datetime
import os

clientm = pymongo.MongoClient(os.getenv("clientm"))
quizdb = clientm.Quiz
setscol = quizdb.Sets


def all_sets():
    sets = []
    for set in setscol.find().sort("Priority", 1):
        sets.append(set)
    return sets


def add_set(set_id, set_name, set_type, set_creator, set_words, priority):
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
        "Priority": priority,
        "Created": current_date,
    }]
    setscol.insert_many(document)


def get_set(set_id):
    myquery = {"_id": set_id}
    for quiz_set in setscol.find(myquery):
        return quiz_set
    return False


def add_set_play(set_id):
    quiz_set = get_set(set_id)
    if not quiz_set:
        return False
    plays = quiz_set['Plays'] + 1
    del quiz_set['Plays']
    quiz_set['Plays'] = plays
    setscol.delete_one({"_id": quiz_set['_id']})
    setscol.insert_many([quiz_set])
