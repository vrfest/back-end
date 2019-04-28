from bson.objectid import ObjectId

class TicketController():
    def __init__(self, db):
        self.db = db

    def get_all_tickets(self):
        ticket_cursor = self.db.tickets.find({})
        tickets = []
        for document in ticket_cursor:
            document['_id'] = str(document['_id']) # this is a shitty hack for the json serializer
            tickets.append(document)

        response = {
            "ticket": tickets
        }

        return response
    #
    # def search_tickets(self, search_str):
    #     pass


    def get_ticket(self, ticket_id):
        ticket = self.db.tickets.find_one({"_id": ObjectId(ticket_id)})
        ticket['_id'] = str(ticket['_id']) # this is a shitty hack for the json serializer

        response = {
            "ticket": ticket
        }

        return response


    def buy_ticket(self, user_id):
        pass