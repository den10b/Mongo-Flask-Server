from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    message = db.Column(db.String(120))

    def __repr__(self):
        return '<Messageser {}>'.format(self.name)

