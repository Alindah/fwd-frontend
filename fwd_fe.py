"""
This app returns the length of a given string.

"""
from flask import Flask, request, render_template
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

backend_ip = "http://localhost:5000/"
some_user = { 'name': 'Guest' }
def_val = "Hello World!"

@app.route('/')
def index():
	return render_template("index.html", user=some_user, form_in=def_val)

@app.route('/', methods = ['POST'])
def send_form():
	user_str = request.form['usr_input']
	res = requests.post(backend_ip, data=request.form)
	return render_template("index.html", user=some_user, form_in=user_str, res=res.text)

if __name__ == '__main__':
	# Note: Can't choose localhost as host because it will not work with Docker
    # app.run(debug=True, host="localhost", port=8000)
	app.run(debug=True, host="0.0.0.0", port=8000)

