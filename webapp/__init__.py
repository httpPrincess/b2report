from flask import Flask
from flask.ext.uploads import UploadSet, TEXT, configure_uploads
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

import os


if not os.path.exists('./uploads/'):
    print 'Upload path does not exist'
    exit(1)

app = Flask(__name__)
app.secret_key = 'zbada1001021'
Bootstrap(app)

# uploads:
path = os.path.abspath('./uploads/')
app.config['UPLOADS_DEFAULT_DEST'] = path
text_files = UploadSet('texts', TEXT)
configure_uploads(app, text_files)

# database:
database_file = 'data/resources.db'
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///%s' % database_file)
db = SQLAlchemy(app)

import views