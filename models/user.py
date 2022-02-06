from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer
from flask_login import UserMixin
from datetime import datetime
from . import db


class User(db.model, UserMixin):

    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincerement=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')


@property
def password(self):
    raise AttributeError('You cannot read this attribute')


@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)


def verify_password(self, password):
    return check_password_hash(self.password_hash, password)


def save_u(self):
    db.session.add(self)
    db.session.commit()


def delete(self):
    db.session.delete(self)
    db.session.commit()


def __repr__(self):
    return f'User {self.username}'
