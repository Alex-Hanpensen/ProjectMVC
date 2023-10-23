from marshmallow import Schema, fields
from app.setup_db import db


class User(db.Model):
    """
    creating a model
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)


class UserSchema(Schema):
    """
    Data Serialization
    """
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
