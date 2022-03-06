from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    history = db.relationship('History', backref = 'history')
    first_name = db.Column(db.String(120), nullable = False)
    last_name = db.Column(db.String(120), nullable = False)
    user_name = db.Column(db.String(120), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    hashed_password = db.Column(db.String(20), nullable = False)
    is_admin = db.Column(db.Boolean(), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def __repr__(self) -> str:
        return f'user_name: {self.user_name}, id: {self.user_id}'

class History(db.Model):
    history_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

