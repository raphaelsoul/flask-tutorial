__author__ = 'scb53'

from app import app

@app.route('/')
@app.route('/index')
def index():
	return "hello, here is index!"