#!/usr/bin/env python
from webapp import db
import os

if not os.path.exists('./uploads/'):
    print 'Upload path does not exist'
    os.mkdir('./uploads')
    exit(1)


# db init
os.mkdir('webapp/data')
db.create_all()
