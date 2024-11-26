from app import db

class User(db.Model):
    __tablename__ = 'bars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))
    number = db.Column(db.String(20))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    open_hours = db.Column(db.String(100))
