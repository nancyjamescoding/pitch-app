import secrets
import os


class Base:
    FLASK_APP='main.py'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = secrets.token_hex(16)

class Development(Base):
    FLASK_DEV = "development"   
    # DATABASE = os.envirom.get("DATABASE")
    DATABASE = ''
    POSTGRES_USER = ''
    POSTGRES_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/pomodor.db'
class Production(Base):
    FLASK_DEV = "development"   
    # DATABASE = os.envirom.get("DATABASE")
    DATABASE = ''
    POSTGRES_USER = ''
    POSTGRES_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/pomodor.db'   