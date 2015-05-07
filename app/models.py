from app import db
import datetime



class User(db.Model):  
    id = db.Column(db.Integer, primary_key = True)
    phonenum = db.Column(db.String(20), index = True)
    pw_hash = db.Column(db.String(255))
    join_datetime = db.Column(db.DateTime())
    
class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	question_text = db.Column(db.String(255))
	created_datetime = db.Column(db.DateTime())
	daily_time = db.Column(db.Time())
	state = db.Column(db.Integer())

	def __init__(self, question_text):
		self.question_text=question_text


class Response(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sent_datetime = db.Column(db.DateTime())
	reply = db.Column(db.String(255))

	def __init__(self):
		self.sent_datetime=datetime.datetime.utcnow()
