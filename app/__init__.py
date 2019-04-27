import sys
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
MONGODB_URI = os.getenv('MONGODB_URI', "")
app.config["MONGO_URI"] = MONGODB_URI
mongo = PyMongo(app)

@app.route('/')
def index():
	online_users = mongo.db.users.find()
	print(online_users)

	return render_template("index.html")
