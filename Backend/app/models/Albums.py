import os
import json
from flask import jsonify
from . import db

class Album(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), name="name", nullable=False, unique=True)
    photos = db.relationship('Photo', backref='album', lazy=True)
    active = db.Column(db.Boolean, name="active", default=False, nullable=False)

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": f"{self.name}",
            "photos": json.dumps([i.serialize() for i in self.photos]),
            "active": self.active,
        }

    def serialize_cover(self):
        return {
            "id": self.id,
            "name": f"{self.name}",
            "photos": json.dumps([i.serialize() for i in self.photos if i.cover]),
            "active": self.active,
        }
