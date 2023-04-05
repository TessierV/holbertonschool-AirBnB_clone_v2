#!/usr/bin/python3
"""Script that starts a web application"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)

def teardown_data(self):
    """ refresh data """
    storage.close()

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    states = storage.all(State).values()
    states_none = None
    for state in states:
        if id == state.id:
            states_none = state
            break
    return render_template('9-states.html', states=states, id=id, states_none=states_none)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)