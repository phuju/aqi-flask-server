from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route('/')
def home():
    return "Flask server is active"

@app.route('/send-data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    print("Received data:", data)
    if data:
        latest_data = data
        return jsonify({'status': 'received'}), 200
    return jsonify({'status': 'error'}), 400

@app.route('/data', methods=['GET'])
def send_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run()
