import os
import vimeo
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask.views import MethodView
from werkzeug.exceptions import abort
from ..models import db
from ..models.Video import Video


videoapi = Blueprint('videoapi', __name__, url_prefix='/video')

def add_video(data):
    video = {}
    current = Video.query.filter_by(name=data['name']).all()
    if current:
        return "Video already in database"
    video['name']: str = data['name']
    video['link']: str = data['link']
    video['uri']: str = data['uri'].replace('/videos/', '/video/')
    for picture in data['pictures']['sizes']:
        if picture['width'] == 640:
            video['image_small']: str = picture['link']
        elif picture['width'] == 960:
            video['image_large'] = picture['link']
    updater = Video(name=video['name'],
                        link=video['link'],
                        uri=video['uri'],
                        host='vimeo',
                        image_small=video['image_small'],
                        image_large=video['image_large'],
                        OnHome=False
                        )
    db.session.add(updater)
    db.session.commit()
    return "Video successfully added to database"

class VideoAPI(MethodView):
    def get(self, video_id):
        if video_id is None:
            return jsonify([i.serialize() for i in Video.query.all()])
        else:
            return Video.query.filter_by(id=video_id).first_or_404().serialize()

    def post(self):
        url = request.form['url']
        uri = url.rfind("/")
        if uri == -1:
            return ("Invalid URI", 404)
        personal_token: str = os.getenv("PAT")
        client_id: str = os.getenv("CID")
        secret_key: str = os.getenv("SAT")
        video = f"https://api.vimeo.com/videos{url[uri:]}"
        client = vimeo.VimeoClient(
            token=personal_token,
            key=client_id,
            secret=secret_key
        )
        response = client.get(video)
        if response.status_code == 200:
            data = response.json()
            return add_video(data)
        else:
            return "Ivalid URL"

    def put(self):
        pass

    def delete(self):
        pass


@videoapi.route('/home', methods=['GET'])
def onhome():
    return jsonify([x.serialize() for x in
                    Video.query.filter_by(OnHome=True).all()])


video_view = VideoAPI.as_view('video_api')
videoapi.add_url_rule('/', defaults={'video_id': None}, view_func=video_view,
                      methods=['GET'])
videoapi.add_url_rule('/', view_func=video_view, methods=['POST'])
videoapi.add_url_rule('/<int:video_id>', view_func=video_view, methods=['GET'])
