from flask import Blueprint, request, jsonify
from ..db.models.users import User
from ..app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Create the Blueprint for users
users_bp = Blueprint('users', __name__)

# Secret key for encoding JWTs (keep this safe, you may want to store it in environment variables)
SECRET_KEY = 'su_ema'


# Register new user
@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Hash the password before storing it using pbkdf2:sha256
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    new_user = User(
        username=data['username'],
        password=hashed_password,  # Store the hashed password
        email=data['email']
    )

    db.session.add(new_user)
    db.session.commit()

    # Create JWT token after successful registration
    token = jwt.encode({
        'user_id': new_user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'User created successfully', 'token': token}), 201


# User login
@users_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and check_password_hash(user.password, data.get("password")):
        # Generate JWT token on successful login
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'message': 'Login successful', 'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


# Fetch all users (for testing or admin purposes)
@users_bp.route('/users', methods=['GET'])
def fetch_users():
    try:
        users = User.query.all()
        return jsonify(users=[{
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "registration_date": user.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        } for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
