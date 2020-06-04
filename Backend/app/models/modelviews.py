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
from .Photos import Photo
from flask import flash
from sqlalchemy.orm.base import instance_state
from . import db
from .. import images

log = logging.getLogger("flask-admin.sqla")


class MyModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


def _list_thumbnail(view, context, model, name):
    if not model.filename:
        return ''

    return Markup(
        '<img src="{model.url}" style="width: 150px;">'.format(model=model)
    )


def _imagename_uuid_gen(obj, file_data, format):
    uid = uuid.uuid1()
    return secure_filename(f"{uid}.{format}".lower())


class MultipleImageUploadInput(object):
    empty_template = "<input %(file)s multiple>"

    # display multiple images in edit view of flask-admin
    data_template = ("<div class='image-thumbnail'>"
                     "   %(images)s"
                     "</div>"
                     )

    def __call__(self, field, **kwargs):

        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)

        args = {
            "file": html_params(type="file", **kwargs),
        }

        if field.data and isinstance(field.data, string_types):

            attributes = self.get_attributes(field)

            args["images"] = "&emsp;".join(["<img src='{}' />".format(src, filename) for src, filename in attributes])

            template = self.data_template

        else:
            template = self.empty_template

        return HTMLString(template % args)

    def get_attributes(self, field):

        filename = field.data

        if field.url_relative_path:
            filename = urljoin(field.url_relative_path, filename)

        yield filename, field.data


class MultipleImageUploadField(ImageUploadField):

    widget = MultipleImageUploadInput()

    def process(self, formdata, data=unset_value):

        self.formdata = formdata  # get the formdata to delete images
        return super(MultipleImageUploadField, self).process(formdata, data)

    def process_formdata(self, valuelist):

        self.data = list()

        for value in valuelist:
            if self._is_uploaded_file(value):
                self.data.append(value)

    def populate_obj(self, obj, name):

        field = getattr(obj, name, None)

        if field:
            if field + "-delete" in self.formdata:
                self._delete_file(field)
                field.remove(field)

        else:
            if self._is_uploaded_file(data):

                self.image = Image.open(data)

                #p = Photo(filename=filename, album_id=obj.id,)
                # db.session.add(p)



class ImageView(ModelView):

    column_list = [
        'album', 'image', 'filename', 'cover'
    ]

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {'filename': MultipleImageUploadField("Photos",
                                                              base_path="app/static/images",
                                                              url_relative_path="/static/images/",
                                                              thumbnail_size=(400, 300, 1))}

    def create_model(self, form):
        try:
            delete_list = []
            for data in form.data['filename']:
                with Image.open(data) as image:
                    filename = _imagename_uuid_gen(object, data, image.format)
                data.seek(0)
                filename = images.save(data, name=filename)
                delete_list.append(images.path(filename))
                album_id=form.data['album'].id
                print(f"album id is: {album_id}")
                photo = Photo(filename=filename,
                              album_id=form.data['album'].id)
                self.session.add(photo)
            self.session.commit()

        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s',
                              error=str(ex)), 'error')
                log.exception('Failed to create record.')

            for path in delete_list:
                os.remove(path)

            self.session.rollback()

            return False
        return photo


class AlbumView(ModelView):

    column_list = [
        'name', 'active'
    ]
