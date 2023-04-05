#!/usr/bin/python3
"""
    Create flask application instance (app)
"""

from flask import Flask, render_template
from markupsafe import escape
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
        after each request : remove current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
        Display a HTML page:
        h1 tag "States"
        UL tag list of all State objects present in DBStorage
            sorted by name(A->Z)
            LI tag : description of one State:<state.id>: <B><state.name></B>
    """
    states = storage.all(State)

    if states:
        states_list = sorted(states.values(), key=lambda x: x.name)
    else:
        states_list = []
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
