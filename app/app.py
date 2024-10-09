import logging
import random
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

LOG_PATH = os.getenv('LOG_PATH', 'app_logs.log')
PORT = int(os.getenv('PORT', 5000))

logging.basicConfig(filename=LOG_PATH, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    logging.info("Home endpoint accessed")
    return jsonify(message="Welcome to the demo app!")


@app.route('/simulate')
def simulate():
    log_type = request.args.get('type')
    
    if not log_type:
        log_type = random.choice(["INFO", "WARNING", "ERROR"])

    if log_type.upper() == "INFO":
        logging.info("Info log generated via simulate")
    elif log_type.upper() == "WARNING":
        logging.warning("Warning log generated via simulate")
    elif log_type.upper() == "ERROR":
        logging.error("Error log generated via simulate")
    else:
        return jsonify(message="Invalid log type! Please use INFO, WARNING, or ERROR."), 400

    return jsonify(message=f"{log_type} log generated!")


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
