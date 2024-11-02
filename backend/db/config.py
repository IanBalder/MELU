import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://user:password@db:5432/database")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
