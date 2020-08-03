from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)
from flask.views import MethodView
from ..models.Albums import Album

albumapi = Blueprint('albumapi', __name__, url_prefix='/album')


class AlbumAPI(MethodView):
    def get(self, album_id):
        if album_id is None:
            return jsonify([i.serialize() for i in Album.query.all()])
        else:
            return Album.query.filter_by(id=album_id).first_or_404().serialize()


class AlbumCoverAPI(MethodView):
    def get(self):
        return jsonify([i.serialize_cover() for i in Album.query.all() if
                        i.active for y in i.photos if y.cover])


album_view = AlbumAPI.as_view('album_api')
album_cover_view = AlbumCoverAPI.as_view('album_cover_api')
albumapi.add_url_rule(
    '/', defaults={'album_id': None}, view_func=album_view, methods=['GET'])
albumapi.add_url_rule('/<int:album_id>', view_func=album_view, methods=['GET'])
albumapi.add_url_rule('/cover', view_func=album_cover_view, methods=['GET'])
