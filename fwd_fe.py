"""
This app returns the length of a given string.

"""
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

some_user = { 'name': 'Guest' }
def_val = "Hello World!"

@app.route('/')
def index():
	return render_template("index.html", user=some_user, form_in=def_val)

@app.route('/', methods = ['POST'])
def send_form():
	data = request.form['num_input']
	return render_template("index.html", user=some_user, form_in=data, res=len(data))

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)

