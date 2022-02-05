import requests
from flask import Flask
from flask import render_template


app=Flask(__name__)
app.config['SECRET_KEY']='CliveTHOMPSONISMAIN'

if __name__=='__main__':
    app.run(debug=True)