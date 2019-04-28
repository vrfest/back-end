import sys
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
MONGODB_URI = os.getenv('MONGODB_URI', "")
client = MongoClient(MONGODB_URI)
db = client['heroku_q29ztbtc']


@app.route('/')
def index():
	online_users = db.users.find_one()
	print(str(online_users['first_name']))
	set_password(online_users) 
	#print(check_password(db,online_users['password']))
	return render_template("index.html")

def set_password(self):
    self['password'] = generate_password_hash("motherfuck")

def check_password(self, password):
    return check_password_hash(self.password_hash, password)

""" 
@app.route('/signup')
def signup():
    if request.method == 'POST':
        print("received request")
        print(str(request))

        email = request.form['email']
        password = request.form['password']
        print(email, password)
        try:
            user = db.create_user_with_email_and_password(email, password)
            # TODO: print message to frontend: account created!
            print("account created!")
        except requests.exceptions.HTTPError as e:
            errormsg = str(e)
            print(errormsg)
            err = errormsg.split('{')[2].split(',')[1].split(':')[1].strip().replace("\"", "").replace("_", " ").lower()
            # TODO:  print message to frontend: err
            print("error: "+str(err))
            return redirect(url_for('signup'))
        results = db.child("users")
    return json.dumps({'success':True}), 200

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)	

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
"""



