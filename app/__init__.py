import sys
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
MONGODB_URI = os.getenv('MONGODB_URI', "")
client = MongoClient(MONGODB_URI)
db = client['heroku_q29ztbtc']

@app.route('/')
def index():
	online_users = db.users.find_one()
	print(str(online_users))

	return render_template("index.html")
