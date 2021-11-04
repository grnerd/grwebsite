'''
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
	id = db.Colunm(db.Integer, primary_key=True)
	email = db.Colunm(db.String(150), unique=True)
	usrname = db.Colunm(db.String(150), unique=True)
	password = db.Colunm(db.String)
	date_created = db.Colunm(db.DateTime(timezone=True), default=func.now())
'''