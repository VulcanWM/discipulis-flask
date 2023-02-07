from flask import session


def add_cookie(key, value):
    session[key] = value


def del_cookies():
    session.clear()


def get_cookie(key):
    if x := session.get(key):
        return x
    else:
        return False
