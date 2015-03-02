
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from webapp import text_files

from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(Form):
    file = FileField('file', validators=[
        FileRequired(),
        FileAllowed(text_files, 'Text files only!')
    ])
    description = StringField('description', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        return Form.validate(self)


class GeneratorForm(Form):
    data_set = RadioField('data_set', validators=[])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
