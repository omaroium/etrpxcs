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
  "measurementId": "G-LT58HQDH4E",
  "databaseURL":"https://entrpxcs-default-rtdb.europe-west1.firebasedatabase.app/"

}
firebase=pyrebase.initialize_app(Config)
auth = firebase.auth()
db=firebase.database()
#Initialize Firebase


@app.route('/', methods=['GET', 'POST'])
def home():
    error = ""
    if request.method == 'POST':
            error = "Authentication failed"
    return render_template("home.html")


@app.route('/findus', methods=['GET', 'POST'])
def findus():
    error = ""
    if request.method == 'POST':
            error = "Authentication failed"
    return render_template("index.html")

@app.route('/questions', methods=['GET', 'POST'])
def survey():
    error = ""
    if request.method == 'POST':
        answers={"i":request.form['i'],"ii":request.form['ii'], "iii":request.form['iii'],"iiii":request.form['iiii'],"s":request.form['s'], "si":request.form['paragraph_text']}
        db.child("Answers").push(answers)
        return redirect(url_for('home'))
    return render_template("question.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
    error = ""
    if request.method == 'POST':

            error = "Authentication failed"
    return render_template("display.html",answers=db.child('Answers').child().get().val())


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)


