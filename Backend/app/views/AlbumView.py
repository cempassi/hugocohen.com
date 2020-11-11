import flask_login as login
from flask_admin.contrib.sqla import ModelView

class AlbumView(ModelView):

    column_list = [
        'name', 'active'
    ]

    def is_accessible(self):
        return login.current_user.is_authenticated
