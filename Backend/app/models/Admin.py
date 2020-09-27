import os
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120))
    about = db.Column(db.Text())
    clients = db.Column(db.Text())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.login

    def serialize(self):
        return {
            "id": self.id,
            "about": f"{self.about}",
            "clients": f"{self.clients}"
        }

    def init():
        if not Administrator.query.all():
            login = os.getenv('ADMIN_LOGIN')
            password = generate_password_hash(os.getenv('ADMIN_PASSWD'))
            email = os.getenv('ADMIN_MAIL')
            admin = Administrator(login=login, password=password, email=email)
            db.session.add(admin)
            db.session.commit();

