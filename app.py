# backend/app.py
from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Print current working directory and files
print("Current Working Directory:", os.getcwd())
print("Files in Directory:", os.listdir(os.getcwd()))

# Load CSV data
try:
    df = pd.read_csv("cgggg.csv")
    print("Successfully loaded file.csv")
except FileNotFoundError:
    print("Error: file.csv not found. Please place it in the same directory as app.py.")
    exit(1)

@app.route("/data", methods=["GET"])
def get_data():
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)