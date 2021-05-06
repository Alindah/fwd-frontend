import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or "shh this is a secret"
	DEF_VAL = os.environ.get('DEF_VAL') or "Hello World!"
	BACKEND_IP = os.environ.get('BACKEND_IP') or "http://localhost:5000/"