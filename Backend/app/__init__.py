import os
import flask_admin as admin
import flask_login as login
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_admin.contrib.sqla import ModelView
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from .models import db

images = UploadSet('images', IMAGES)
migrate = Migrate()

def load_user(admin_id):
    from .models.Admin import Administrator
    return db.session.query(Administrator).get(admin_id)

def init_login(app):
    login_manager = login.LoginManager()
    login_manager.user_loader(load_user)
    login_manager.init_app(app)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_envvar('SETTINGS_PATH')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    CORS(app, origins=["https://hugocohen.com", "http://localhost:8080"])
    configure_uploads(app, (images))
    patch_request_class(app)
    # initialize the database
    db.init_app(app)
    migrate.init_app(app, db)
    from .api.sync import bp as sync
    from .api.video import videoapi
    from .api.album import albumapi

    from .models.Admin import Administrator
    from .views.AdminView import AdminView
    from .models.Video import Video
    from .views.VideoView import VideoView
    from .models.Photos import Photo
    from .views.PhotoView import PhotoView
    from .models.Albums import Album
    from .views.AlbumView import AlbumView
    from .api.admin import MyAdminIndexView, aboutapi

    init_login(app)
    app.register_blueprint(sync)
    app.register_blueprint(videoapi)
    app.register_blueprint(albumapi)
    app.register_blueprint(aboutapi)
    a = admin.Admin(app, name="hugoweb", index_view=MyAdminIndexView(),
                        base_template='admin/my_master.html', template_mode="bootstrap3")
    a.add_view(VideoView(Video, db.session))
    a.add_view(AdminView(Administrator, db.session))
    a.add_view(AlbumView(Album, db.session))
    a.add_view(PhotoView(Photo, db.session))

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Init administrator if not present
    with app.app_context():
        #Administrator.init()
        return app
