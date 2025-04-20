from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running!"

# ✅ This is the important part for your ESP32:
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received Data:", data)
    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
