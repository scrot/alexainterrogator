#!/usr/bin/env python3
from flask import Flask, request, json, url_for, render_template
from flask_socketio import SocketIO, emit, send
from json import dumps
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = "random"
socketio = SocketIO(app)

RESPONSE = {}

@socketio.on('answer', namespace="/answers")
def incomming_answer(r):
    global RESPONSE
    print('received answer from person' + r.get('person') + ': ' + str(r))
    RESPONSE = r
    print(RESPONSE)


@app.route('/ask/<person>', methods=['POST'])
def incomming_question(person):
    """
    handle incomming question
    """
    global RESPONSE
    RESPONSE = {}

    r = request.get_json()
    print("received question for person " + person + ": " + str(r))
    socketio.emit('question', r, namespace="/person/" + person)
    
    while(RESPONSE.get('person') != person):
        exit = RESPONSE.get('answer')
        if exit == 'exit':
            return json.dumps({'person':'None', 'answer': 'I am requested to skip this question'})
    return json.dumps(RESPONSE)



@app.route('/person/<person>', methods=['GET'])
def person(person):
    """
    Render the person-page'
    """
    url_for('static', filename='style.css')
    url_for('static', filename='ws.js')
    url_for('static', filename='logo.png')
    return render_template('person.html', p=person)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80, debug=False)
