from flask import Flask, jsonify
from flask_cors import CORS
import json


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/json', methods=['GET'])
def getMetaData():
    with open('PIA04216_orig.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    app.run()
