from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

DATA_FILE = "sensor_data.json"
stored_data = []

# Load existing data (if any)
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)

def validate_sensor_data(data):
    required_fields = ["temp", "hum", "CO2", "dust", "AQI"]
    return all(field in data and isinstance(data[field], (int, float)) for field in required_fields)

@app.route('/send-data', methods=['POST'])
def receive_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    if not validate_sensor_data(data):
        return jsonify({"error": "Invalid data format"}), 400
    
    stored_data.append(data)
    
    # Save to file
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f)
    
    return jsonify({'status': 'success'})

@app.route('/data', methods=['GET'])
def show_data():
    return jsonify(stored_data)

@app.route('/')
def home():
    return "Flask server is active. Use /send-data (POST) and /data (GET)."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
