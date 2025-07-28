from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/api/data')
def data():
    return jsonify({"value": 42})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
