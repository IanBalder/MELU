from flask import Blueprint, request, jsonify
from ..db.models.bars import Bar
from ..app import db

bars_bp = Blueprint('bars', __name__)

test_data = [
    {
        "id": 1,
        "name": "The Tipsy Tavern",
        "email": "contact@tipsytavern.com",
        "address": "123 Main Street, Springfield",
        "number": "555-1234",
        "description": "A cozy bar with a wide selection of craft beers.",
        "image": "https://example.com/images/tipsytavern.jpg",
        "open_hours": "Mon-Fri: 4 PM - 12 AM, Sat-Sun: 2 PM - 1 AM",
    },
    {
        "id": 2,
        "name": "Moonlight Lounge",
        "email": "info@moonlightlounge.com",
        "address": "456 Elm Street, Rivertown",
        "number": "555-5678",
        "description": "A chic cocktail bar offering live music every weekend.",
        "image": "https://example.com/images/moonlightlounge.jpg",
        "open_hours": "Mon-Sun: 5 PM - 2 AM",
    },
    {
        "id": 3,
        "name": "The Rustic Barrel",
        "email": "hello@rusticbarrel.com",
        "address": "789 Oak Avenue, Lakeside",
        "number": "555-9101",
        "description": "A country-style bar with great BBQ and live sports.",
        "image": "https://example.com/images/rusticbarrel.jpg",
        "open_hours": "Mon-Fri: 3 PM - 11 PM, Sat-Sun: 12 PM - 12 AM",
    },
    {
        "id": 4,
        "name": "Urban Retreat",
        "email": "contact@urbanretreat.com",
        "address": "321 Market Street, Metropolis",
        "number": "555-1122",
        "description": "A modern bar with rooftop views and an extensive wine list.",
        "image": "https://example.com/images/urbanretreat.jpg",
        "open_hours": "Mon-Fri: 5 PM - 11 PM, Sat-Sun: 4 PM - 12 AM",
    },
    {
        "id": 5,
        "name": "The Happy Hour Hideout",
        "email": "info@happyhourhideout.com",
        "address": "654 Pine Lane, Uptown",
        "number": "555-3344",
        "description": "A vibrant bar with happy hour specials and karaoke nights.",
        "image": "https://example.com/images/happyhourhideout.jpg",
        "open_hours": "Mon-Fri: 4 PM - 10 PM, Sat-Sun: 3 PM - 11 PM",
    },
]

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
def fetch_bars():
    return jsonify(test_data)
    try:
        bars = Bar.query.all()
        return jsonify(bars=[{
            "id": bar.id,
            "name": bar.name,
            "email": bar.email,
            "address": bar.address,
            "number": bar.number,
            "description": bar.description,
            "image": bar.image,
            "open_hours": bar.open_hours,
        } for bar in bars]), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
