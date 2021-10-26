import datetime,mysql.connector
from portfolio import db


class Message(db.Model):
    sender_id =  db.Column(db.Integer(),primary_key=True,autoincrement=True)
    sender_name = db.Column(db.String(255),nullable=False)
    sender_email = db.Column(db.String(255),nullable=False)
    sender_message = db.Column(db.String(255),nullable=False)