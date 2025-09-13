from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import psutil

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "App")
    return f"Hello {app_name} 🚀"

@app.route("/status")
def status():
    return jsonify({"status": "ok"}), 200

@app.route("/metrics")
def metrics():
    # Example metrics
    memory = psutil.virtual_memory()
    return jsonify({
        "cpu_percent": psutil.cpu_percent(),
        "memory_total": memory.total,
        "memory_used": memory.used
    }), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
