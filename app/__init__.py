import os
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

from app.ticket import TicketController

app = Flask(__name__, static_url_path='')
MONGODB_URI = os.getenv('MONGODB_URI', "")
client = MongoClient(MONGODB_URI)
db = client['heroku_q29ztbtc']

@app.route('/')
def index():
	return app.send_static_file("index.html")


# React routes
@app.route('/homepage')
def homepage():
	return app.send_static_file("index.html")
# React routes
@app.route('/login')
def login():
	return app.send_static_file("index.html")
# React routes
@app.route('/signup')
def signup():
	return app.send_static_file("index.html")
# React routes
@app.route('/dashboard')
def dashboard():
	return app.send_static_file("index.html")
# React routes
@app.route('/payment')
def payment():
	return app.send_static_file("index.html")
# React routes
@app.route('/test')
def test():
	return app.send_static_file("index.html")



# @app.route('/tickets/create', methods=['POST'])
# def buy_ticket():
#
# 	return ""
# 	#return jsonify(TicketController(db).get_all_tickets())

@app.route('/tickets', methods=['GET'])
def get_all_tickets():
	return jsonify(TicketController(db).get_all_tickets())

@app.route('/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
	return jsonify(TicketController(db).get_ticket(ticket_id))

# @app.route('/tickets/<ticket_id>')
# def search_tickets(search_str):
# 	return ""