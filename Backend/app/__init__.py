import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_envvar('YOURAPPLICATION_SETTINGS')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # initialize the database
    db.init_app(app)
    from . import utils
    from . import video
    app.register_blueprint(utils.bp)
    app.register_blueprint(video.bp)
    with app.app_context():
        db.create_all()  # Create database tables for our data models

        return app

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World, we are running live!'

    return app
