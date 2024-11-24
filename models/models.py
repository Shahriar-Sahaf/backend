from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return self.username

class CalculationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input1 = db.Column(db.Float, nullable=False)
    input2 = db.Column(db.Float, nullable=False)
    input3 = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)