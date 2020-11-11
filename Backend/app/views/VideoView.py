import os
import uuid
import ast
import logging
import imghdr
from flask_admin.babel import gettext
from PIL import Image
import flask_login as login
from flask import Markup
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import BaseForm
from flask_admin import form
from wtforms.fields import MultipleFileField
from werkzeug.utils import secure_filename
from wtforms.widgets import html_params, HTMLString
from wtforms.utils import unset_value
from flask_admin.helpers import get_url
from flask_admin.form.upload import ImageUploadField
from flask_admin._compat import string_types, urljoin
from ..models.Video import Video

from flask import flash
from sqlalchemy.orm.base import instance_state
from . import db
from .. import images

log = logging.getLogger("flask-admin.sqla")

def _imagename_gen(ob, video):
    uid = uuid.uuid1()
    with Image.open(video) as image:
        imagename = secure_filename(f"{uid}.{image.format}".lower())
    return imagename
        

class VideoView(ModelView):

    column_list = [
        'name', 'link', 'host', 'uri', 'OnHome'
    ]

    form_extra_fields = {
            'image': ImageUploadField('Image',
            base_path='/app/static/images/video',
            url_relative_path="/static/video/images/",
            namegen=_imagename_gen,
            thumbnail_size=(400, 300, 1))
            }


    def is_accessible(self):
        return login.current_user.is_authenticated

