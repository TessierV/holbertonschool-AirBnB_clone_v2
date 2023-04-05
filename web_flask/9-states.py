#!/usr/bin/python3
""" doc """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
def listStates():
    States = storage.all(State)
    Cities = storage.all(City)

    return render_template("9-states.html", states=States, cities=Cities)


@app.route("/states/<id>", strict_slashes=False)
def listStateCities(id):
    Citis = storage.all(City)
    StatesList = storage.all(State)
    for state in StatesList.values():
        print(str(state.id) + " ===" + str(id))
        if str(state.id) == str(id):
            return render_template("9-states.html", states=state, cities=Citis)
    return render_template("9-states.html", cities=Citis)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
