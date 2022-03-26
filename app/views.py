import flask

from app import app, db
from .models import Message


@app.route('/post', methods=['POST'])
def sendMessage():
    username = flask.request.values.get('user')  # Your form's
    message = flask.request.values.get('message')  # input names
    db.session.add(Message(name=username, message=message))
    db.session.commit()
    return "200"


@app.route('/get', methods=['GET'])
def getChat():
    msg = []
    for obj in db.session.query(Message).order_by(Message.id):
        msg.append(obj.name+": "+obj.message)
    return str(msg)

