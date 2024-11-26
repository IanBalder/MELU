from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .models import User
from .config import Config