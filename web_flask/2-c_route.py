#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """display “Hello HBNB!”"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    return("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
