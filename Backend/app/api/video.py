import os
import vimeo
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask.views import MethodView
from werkzeug.exceptions import abort
from ..models import Video


videoapi = Blueprint('videoapi', __name__, url_prefix='/video')


class VideoAPI(MethodView):
    def get(self, video_id):
        if video_id is None:
            return jsonify([i.serialize() for i in Video.query.all()])
        else:
            return Video.query.filter_by(id=video_id).first_or_404().serialize()
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

video_view = VideoAPI.as_view('video_api')
videoapi.add_url_rule('/', defaults={'video_id': None}, view_func=video_view,
                methods=['GET'])
videoapi.add_url_rule('/<int:video_id>', view_func=video_view, methods=['GET'])
