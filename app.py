from flask import Flask
import os

app = Flask(__name__)

LOG_FILE = "/data/logs.txt"

@app.route('/')
def home():
    with open(LOG_FILE, "a") as f:
        f.write("New visit!\n")
    return "Hello, World! Check logs in /data/logs.txt."

if __name__ == "__main__":
    os.makedirs("/data", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
