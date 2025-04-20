from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route('/', methods=['GET'])
def home():
    return "Flask server is active"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

@app.route('/send-data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    if data:
        print("Received:", data)
        latest_data = data
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'no data received'}), 400
