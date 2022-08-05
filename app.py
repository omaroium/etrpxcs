from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
from datetime import datetime

tweet={}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {
  "apiKey": "AIzaSyB1nL_aDIG_HdYXfVXj_oqLXJjSxnzUPCk",
  "authDomain": "entrpxcs.firebaseapp.com",
  "projectId": "entrpxcs",
  "storageBucket": "entrpxcs.appspot.com",
  "messagingSenderId": "200107293232",
  "appId": "1:200107293232:web:77d0ecb423c4e82ed90bf5",
  "measurementId": "G-LT58HQDH4E"
  "databaseURL":"https://entrpxcs-default-rtdb.europe-west1.firebasedatabase.app/"

}
firebase=pyrebase.initialize_app(Config)
auth = firebase.auth()
db=firebase.database()
#Initialize Firebase


@app.route('/', methods=['GET', 'POST'])
def question():
    error = ""
    if request.method == 'POST':
            error = "Authentication failed"
    return render_template("question.html")


