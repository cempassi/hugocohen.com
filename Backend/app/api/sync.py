import os
import vimeo
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from ..models import db
from ..models.Video import Video

bp = Blueprint('sync', __name__, url_prefix='/sync')


def add_items(data) -> dict:
    videos: dict = {}
    current = Video.query.all()
    for id, info in enumerate(data):
        if info['privacy']['view'] != 'anybody' or any(x.name == info['name']
                                                       for x in current):
            continue
        video: dict = {}
        video['name']: str = info['name']
        video['link']: str = info['link']
        video['uri']: str = info['uri'].replace('/videos/', '/video/')
        updater = Video(name=video['name'],
                        link=video['link'],
                        uri=video['uri'],
                        host='vimeo',
                        OnHome=False
                        )
        db.session.add(updater)
        videos[f"{id}"] = video
    db.session.commit()
    return videos


@bp.route('/', methods=['GET'])
def sync():
    personal_token: str = os.getenv("PAT")
    client_id: str = os.getenv("CID")
    secret_key: str = os.getenv("SAT")
    uri = '/me/videos'
    client = vimeo.VimeoClient(
        token=personal_token,
        key=client_id,
        secret=secret_key
    )
    response = client.get(uri)

    if response.status_code == 200:
        data = response.json()
        return (add_items(data['data']))
