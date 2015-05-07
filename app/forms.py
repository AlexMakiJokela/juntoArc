from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(Form):
	 phone = StringField('phone', validators=[DataRequired()])
	 password = PasswordField('password', validators=[DataRequired()])
	 question = StringField('question')
	 question_time = DateTimeField('question_time')

class MakeQuestionForm(Form):
	 question = StringField('question')
	 question_time = DateTimeField('question_time')