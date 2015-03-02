#!/usr/bin/env python
from webapp import db
import os

if not os.path.exists('./uploads/'):
    print 'Upload path does not exist'
    os.mkdir('./uploads')
# db init
if not os.path.exists('webapp/data/'):
    os.mkdir('webapp/data')

db.create_all()
