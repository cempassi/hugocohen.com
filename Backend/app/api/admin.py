from flask.views import MethodView
from ..models.Admin import Administrator
from ..models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import form, fields, validators,  StringField, SubmitField
from wtforms.validators import data_required
from flask_admin import helpers, expose
import flask_admin as admin
import flask_login as login
from os import getenv
from flask import Blueprint, url_for, redirect, render_template, request, jsonify

aboutapi = Blueprint('aboutapi', __name__, url_prefix='/about')


class AboutAPI(MethodView):
    def get(self):
        return jsonify(Administrator.query.first_or_404().serialize())

about_view = AboutAPI.as_view('aboutapi')
aboutapi.add_url_rule('/', view_func=about_view, methods=['GET'])

class VideoForm(FlaskForm):
    url = StringField('url', validators=[data_required()])
    submit = SubmitField('Add Video')

class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        admin = self.get_admin()

        if admin is None:
            raise validators.ValidationError('Invalid admin')

        if not check_password_hash(admin.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_admin(self):
        return db.session.query(Administrator).filter_by(login=self.login.data).first()


class MyAdminIndexView(admin.AdminIndexView):

    @expose('/', methods=('GET', 'POST'))
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        form = VideoForm(request.form)
        self._template_args['api_url'] = '/sync'
        self._template_args['api_add_vid'] = '/video'
        self._template_args['add_vid'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            admin = form.get_admin()
            login.login_user(admin)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
