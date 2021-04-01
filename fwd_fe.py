"""
This app returns the length of a given string.

"""
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)

