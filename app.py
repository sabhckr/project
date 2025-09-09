from flask import Flask
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "App")
    return f"Hello {app_name} 🚀"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
