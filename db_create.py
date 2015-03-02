#!/usr/bin/env python
from webapp import db
import os

os.mkdir('webapp/data')
db.create_all()
