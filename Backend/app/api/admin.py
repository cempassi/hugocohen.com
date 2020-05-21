from os import getenv
from flask import Blueprint, url_for, redirect, render_template, request
import flask_login as login
import flask_admin as admin
from flask_admin import helpers, expose
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db
from ..models.Admin import Administrator

bp = Blueprint('admin', __name__, url_prefix='/admin')

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

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        self._template_args['api_url'] = '/sync'
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
