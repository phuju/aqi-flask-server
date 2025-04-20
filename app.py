from flask import Flask, request, jsonify

app = Flask(__name__)

# Store data from ESP32 here
stored_data = []

# Endpoint to receive data from ESP32 via POST
@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received:", data)
    stored_data.append(data)
    return jsonify({'status': 'success'})

# Endpoint to show collected data via browser (GET)
@app.route('/', methods=['GET'])
def show_data():
    return jsonify(stored_data)

# Root route
@app.route('/')
def home():
    return "Flask server is active"
