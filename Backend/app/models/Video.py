import os
import uuid
from sqlalchemy import event
from . import db


class Video(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), name="name", nullable=False)
    link = db.Column(db.String(125), name="link", unique=True, nullable=False)
    host = db.Column(db.String(80), name="host", nullable=False)
    uri = db.Column(db.String(125), name="uri", unique=True, nullable=False)
    image = db.Column(db.String(128), name="image", default="", nullable=True)
    OnHome = db.Column(db.Boolean, name="OnHome", default=False, nullable=False)
    Temp = db.Column(db.Boolean, name="Temp", default=False, nullable=False)

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Name {}>'.format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": f"{self.name}",
            "host": f"{self.host}",
            "link": f"{self.link}",
            "uri": f"{self.uri}",
            "image": f"{self.image}",
            "OnHome": self.OnHome
        }
