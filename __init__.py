from flask import Flask
import requests
from flask import Flask
from flask import render_template


app=Flask(__name__)
app.config['SECRET_KEY']='CliveTHOMPSONISMAIN'

from .views import views
from .auth import auth
app.register_blueprint(auth,url_prefix='/')
if __name__=='__main__':
    app.run(debug=True)