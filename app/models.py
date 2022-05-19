from app import db


class Message(db.Document):
    name = db.StringField()
    message = db.StringField()

