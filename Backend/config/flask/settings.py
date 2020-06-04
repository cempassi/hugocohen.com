import os
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{db_host}:{db_port}/{db_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
API_URL = os.getenv('API_URL')
FLASK_ADMIN_SWATCH = 'slate'
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

UPLOADED_IMAGES_DEST = 'app/static/images'
UPLOADED_IMAGES_URL = '/static/images/'

MAX_CONTENT_LENGTH = 240 * 1024 * 1024
