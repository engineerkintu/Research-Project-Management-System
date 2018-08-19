import os

#BASEDIR = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = 'p5ty67trv<3Eid9%$i81'
SQLALCHEMY_DATABASE_URI = 'postgresql://dt_admin:dt2016@localhost/ebrain_db'

TOP_LEVEL_DIR = os.path.abspath(os.curdir)
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/Ebrain/app/static/img/'
UPLOADS_DEFAULT_URL = 'https://localhost:5000/static/img/'

UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/Ebrain/app/static/img/'
UPLOADED_IMAGE_URL = 'https://localhost:5000/static/img/'
