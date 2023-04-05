#!/usr/bin/python3
""" Write a script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models.state import State
from models import storage


app = Flask(__name__)
state_id = None


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()

@app.route("/states", strict_slashes=False)
def states():
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda x: x.name)
    return render_template("9-states.html", states=states_list)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            state_id = state
    return render_template("9-states.html", state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
