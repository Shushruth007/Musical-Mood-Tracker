from flask import Flask, jsonify
from flask_cors import CORS
from python_test import call_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': call_api()})

@app.route('/complex-test')
def yelp_default_test():
    return jsonify({"result": call_api()})