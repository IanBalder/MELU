from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from db.config import Config  # Import Config from the correct location

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

# Initialize DB schema
with app.app_context():
    db.create_all()  # Simplifies initializing tables

from db.models import User  # Import User from the models file

@app.route("/")
def home():
    return jsonify(message="Welcome to the API")

@app.route("/test-insert", methods=["POST"])
def test_insert():
    try:
        new_user = User(name="testuser", email="testuser@example.com")
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User added successfully"), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route("/test-fetch", methods=["GET"])
def test_fetch():
    try:
        users = User.query.all()
        return jsonify(users=[{"id": user.id, "name": user.name, "email": user.email} for user in users])
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
