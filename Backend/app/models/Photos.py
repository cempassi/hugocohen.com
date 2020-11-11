import os
from werkzeug.utils import secure_filename
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import event
from . import db
from .. import images
from .Albums import Album

class Photo(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    filename = db.Column(db.String(128), name="filename",
                         nullable=False, unique=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    cover = db.Column(db.Boolean, name="cover", default=False, nullable=False)

    def __repr__(self):
        return self.filename

    @property
    def url(self):
        return images.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return images.path(self.filename)

    def serialize(self):
        return {
            "id": self.id,
            "filename": f"{self.filename}",
            "album": "{}".format(Album.query.filter_by(id=self.album_id).first().__repr__()),
            "cover": self.cover
        }

@event.listens_for(Photo, 'after_delete')
def del_image(mapper, connection, target):
    if target.filepath is not None:
        try:
            os.remove(target.filepath)
        except OSError:
            pass
