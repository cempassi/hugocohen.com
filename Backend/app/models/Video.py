import uuid
from . import db


class Video(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), name="name", nullable=False)
    link = db.Column(db.String(125), name="link", unique=True, nullable=False)
    uri = db.Column(db.String(125), name="uri", unique=True, nullable=False)
    image_small = db.Column(db.String(125), name="image_small",
                            unique=True, nullable=False)
    image_large = db.Column(db.String(125), name="image_large",
                            unique=True, nullable=False)
    OnHome = db.Column(db.Boolean, name="OnHome", default=False, nullable=False)

    def __repr__(self):
        return '<Name {}>'.format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": f"{self.name}",
            "link": f"{self.link}",
            "uri": f"{self.uri}",
            "image_small": f"{self.image_small}",
            "image_large": f"{self.image_large}",
            "OnHome": f"{self.OnHome}"
        }
