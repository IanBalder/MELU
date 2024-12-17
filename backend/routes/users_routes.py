from flask import Blueprint, request, jsonify
from ..db.models.users import User
from ..app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import re
from functools import wraps

users_bp = Blueprint('users', __name__)
SECRET_KEY = 'su_ema'
EMAIL_REGEX = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            token = token.split(' ')[1] if "Bearer " in token else token
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(*args, **kwargs)
    return decorated

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')

    if not re.match(EMAIL_REGEX, email):
        return jsonify({'error': 'Invalid email format'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email is already in use'}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email']
    )

    db.session.add(new_user)
    db.session.commit()

    token = jwt.encode({
        'user_id': new_user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'User created successfully', 'token': token}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and check_password_hash(user.password, data.get("password")):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'message': 'Login successful', 'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@users_bp.route('/users', methods=['GET'])
@token_required
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

@users_bp.route('/api/check-email', methods=['POST'])
def check_email():
    data = request.json
    email = data.get('email')
    if User.query.filter_by(email=email).first():
        return jsonify({"exists": True}), 200
    return jsonify({"exists": False}), 200
