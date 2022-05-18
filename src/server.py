import os
from flask import Flask, jsonify
from waitress import serve

host = '0.0.0.0'
port = os.environ.get('FLASK_PORT', 8080)
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return jsonify({
        'hello': 'world'
    })

if __name__ == '__main__':
    print('Starting server at http://{}:{}'.format(host, port))
    serve(app, host=host, port=port)
