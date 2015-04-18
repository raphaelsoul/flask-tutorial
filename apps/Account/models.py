from apps import db
from datetime import datetime

class User(db.Model):

	__tablename__='UserManage_User'

	id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(50), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	register_date = db.Column(db.DateTime,default=datetime.utcnow)
	last_login_at = db.Column(db.DateTime,nullable=True)
	last_login_ip = db.Column(db.String(45),nullable=True)

	def __init__(self, name=None, email=None, password=None):
		self.username = name
		self.email = email
		self.password = password

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)
