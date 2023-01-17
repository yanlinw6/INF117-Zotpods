# coding: utf-8
import os
from pathlib import Path
import dotenv

basedir = Path(__file__).resolve().parent
media_dir = basedir / 'web/media'
default_upload_dir = basedir / 'web/media/upload'

if not os.path.exists(default_upload_dir):
    os.makedirs(default_upload_dir, exist_ok=True)

env_file = basedir / '.env'
if not env_file.exists():
    raise FileNotFoundError('.env file is missing')
dotenv.load_dotenv(dotenv_path=env_file, override=False, encoding='utf-8')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    CSRF_ENABLED  = True
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = SECRET_KEY

    BABEL_DEFAULT_LOCALE = 'en_US'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    # email config
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') == 'True'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') == 'True'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 465))
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER
    FLASKY_MAIL_SUBJECT_PREFIX = os.environ.get('FLASKY_MAIL_SUBJECT_PREFIX')
    FLASKY_MAIL_SENDER = os.environ.get('FLASKY_MAIL_SENDER_TITLE'), MAIL_USERNAME

    # ckEditor
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_LANGUAGE = 'en-US'
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_UPLOAD_ERROR_MESSAGE = 'upload failed'
    CKEDITOR_FILE_UPLOADER = 'ck_upload'
    # CKEDITOR_FILE_BROWSER = 'uploaded'
    # CKEDITOR_EXTRA_PLUGINS = ['filebrowser']
    CKEDITOR_ALLOWED_EXTENSIONS = ['jpg', 'gif', 'png', 'jpeg', ]  # 'wav', 'mp3', 'docx', 'doc', 'pdf'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db_test.sqlite3')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    using a high-performance database in production
    """
    DEBUG = False
    # please change database params to yours
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'.format(
        db_user=os.environ.get('DB_USER'),
        db_password=os.environ.get('DB_PASSWORD'),
        db_host=os.environ.get('DB_HOST'),
        db_port=os.environ.get('DB_PORT'),
        db_name=os.environ.get('DB_NAME'),
    )
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,

    default='development'
)
