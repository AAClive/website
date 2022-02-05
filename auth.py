from flask import Blueprint

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "login"

def signup():
    return "sign up"

def logout():
    return "logout"
