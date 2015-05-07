from app import db
import datetime



class User(db.Model):  #design descision! What characteristics do I want the users to have?
    id = db.Column(db.Integer, primary_key = True)
    phonenum = db.Column(db.String(20), index = True)
    pw_hash = db.Column(db.String(255))
    join_datetime = db.Column(db.DateTime())
    
class Arc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	reminder_text = db.Column(db.String(255))
	created_datetime = db.Column(db.DateTime())
	daily_time = db.Column(db.Time())

	def __init__(self, reminder_text):
		

class Message(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sent_datetime = db.Column(db.DateTime())
	reply = db.Column(db.String(255))

	def __init__(self):
		self.sent_datetime=datetime.datetime.utcnow()
