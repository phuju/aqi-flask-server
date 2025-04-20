from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/data", methods=["POST"])
def receive_data():
    content = request.json
    print("Received from ESP32:", content)
    return "Data received!", 200