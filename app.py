import serverless_wsgi
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)