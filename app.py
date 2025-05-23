import os
import logging
from flask import Flask, render_template

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "engine-maintenance-secret-key")

@app.route('/')
def index():
    """Render the engine maintenance documentation page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
