from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
from datetime import datetime

tweet={}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {

}
firebase=pyrebase.initialize_app(Config)
auth = firebase.auth()
db=firebase.database()
#Initialize Firebase



    error = ""
    if request.method == 'POST':
            error = "Authentication failed"
    return render_template("question.html")


