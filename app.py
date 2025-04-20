from flask import Flask, request, jsonify
from flask_cors import CORS  # Important for cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store data from ESP32 here
stored_data = []

# Combined endpoint for both receiving and showing data
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        print("Received:", data)
        stored_data.append(data)
        return jsonify({'status': 'success'})
    else:  # GET
        return jsonify(stored_data)

# Root route just for health check
@app.route('/')
def home():
    return "Flask server is active. Use /data endpoint for ESP32 communication."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
