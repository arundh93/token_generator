import os

from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

os.environ['PEPPER'] = '12345678'
@app.route("/", methods=['POST'])
def tokenize():
    pepper = os.environ['PEPPER']
    return jsonify(list(map(lambda x: hashlib.sha3_256((x + pepper).encode()).hexdigest(), request.json['data'])))


@app.route("/123")
def health():
    return "Welcome"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
