import os
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

from app.ticket import TicketController

app = Flask(__name__)
MONGODB_URI = os.getenv('MONGODB_URI', "")
client = MongoClient(MONGODB_URI)
db = client['heroku_q29ztbtc']

@app.route('/')
def index():
	online_users = db.users.find_one()
	print(str(online_users))

	return render_template("index.html")

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