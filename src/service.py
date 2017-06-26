import os
# import config
import json
import datetime
import logging
from flask import Flask, render_template, request, Response, jsonify, session
from apartment_list.database import Database 

app = Flask(__name__)


@app.route('/servers', methods=['GET'])
def get_servers():
    result = ['Hello1', 'Hello2']
    return Response(json.dumps(result), status=200,
        mimetype='application/json')


@app.route('/find_group/<email>', methods=['GET'])
def find_group(email):
    db = Database()
    result = db.get_group(email)
    print (result)
    return Response(json.dumps(result), status=200,
        mimetype='application/json')

# -----------------------------UI Views---------------------------------------#
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html', user='Shweta')


#------------------------------main func--------------------------------------#
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
