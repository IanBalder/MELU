from flask import Flask, jsonify
from flask_cors import CORS
from .db import db  # Import the `db` instance from db/__init__.py
from .db.config import Config  # Import Config from db/config

from .routes.bars_routes import bars_bp
from .routes.users_routes import users_bp

app = Flask(__name__)
app.config.from_object(Config)  # Load the app configuration
CORS(app)

# Initialize the db with the app
db.init_app(app)

with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(users_bp, url_prefix='/api')
app.register_blueprint(bars_bp, url_prefix='/api')

@app.route("/")
def home():
    return jsonify(message="Welcome to the API")

if __name__ == '__main__':
    app.run(debug=True)
