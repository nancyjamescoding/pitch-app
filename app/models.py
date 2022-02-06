from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


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


def save_user(self):
    db.session.add(self)
    db.session.commit()


def delete(self):
    db.session.delete(self)
    db.session.commit()


def __repr__(self):
    return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    post = db.Column(db.Text(), nullable=False)
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(255), index=True, nullable=False)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitch(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch

    def __repr__(self):
        return f'Pitch {self.post}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey(
        'pitches.id'), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

    def __repr__(self):
        return f"comment:{self.comment}"


@login_manager.user_loader
def load_user(author_id):
    return User.query.get(int(author_id))
