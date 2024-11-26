from flask import Blueprint, request, jsonify
from models.bars import Bar
from app import db

bars_bp = Blueprint('users', __name__)

@bars_bp.route('/bars', methods=['POST'])
def create_user():
    data = request.get_json()
    new_bar = Bar(
        name=data['name'],
        email=data['email'],
        address=data['address'],
        number=data['number'],
        description=data['description'],
        image=data['image'],
        open_hours=data['open_hours'],
    )
    db.session.add(new_bar)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bars_bp.route("/fetch-bars", methods=["GET"])
def test_fetch():
    try:
        bars = Bar.query.all()
        return jsonify(users=[{
            "id": bar.id,
            "name": bar.name,
            "email": bar.email,
            "address": bar.address,
            "number": bar.number,
            "description": bar.description,
            "image": bar.image,
            "open_hours": bar.open_hours,
        } for bar in bars])
    except Exception as e:
        return jsonify(error=str(e)), 500
