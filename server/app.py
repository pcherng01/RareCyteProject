from flask import Flask, jsonify, send_file
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

@app.route('/images/metadata/<name>', methods=['GET'])
def getMetaData(name):
    metadataName = '../resources/images/%s.json' % name
    with open(metadataName) as f:
        data = json.load(f)
    return data

@app.route('/images/<name>', methods=['GET'])
def getImage(name):
    imageName = '../resources/images/%s.jpg' % name
    return send_file(imageName, mimetype='image/gif')


if __name__ == '__main__':
    app.run()
