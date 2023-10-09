from marshmallow import fields, Schema
from app.setup_db import db


class Director(db.Model):
    """
    creating a model
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


#
class DirectorsSchema(Schema):
    """
    Data Serialization
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
