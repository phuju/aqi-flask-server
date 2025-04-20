from flask import Flask, request, jsonify
from flask_cors import CORS  # Required for ESP32 communication

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

stored_data = []

# Handle both POST (from ESP32) and GET (for browser) at the root
@app.route('/', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        print("Received:", data)
        stored_data.append(data)
        return jsonify({'status': 'success'})
    else:  # GET
        return jsonify({"message": "Flask server is running", "data": stored_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
