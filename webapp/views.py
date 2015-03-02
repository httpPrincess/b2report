from flask import request, flash, render_template, redirect, url_for
from markov import MarkovGenerator
from model import Resource
from webapp import app, text_files, db
from webapp.forms import UploadForm, GeneratorForm


def get_generator_form():
    files = Resource.query.all()
    if len(files) == 0:
        return None

    generator_form = GeneratorForm()
    data_sets = [(resource.id, resource.description) for resource in files]
    generator_form.data_set.choices = data_sets
    return generator_form


@app.route('/')
def index():
    return render_template('index.html',
                           generator_form=get_generator_form(),
                           upload_form=UploadForm())


@app.route('/upload', methods=['POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = text_files.save(form.file.data)

        resource = Resource()
        resource.filename = filename
        resource.description = form.description.data
        db.session.add(resource)
        db.session.commit()
        flash('File saved', 'info')
        return redirect(url_for('index'))
    else:
        # not beautiful as we don't change the url but ok
        return render_template('index.html',
                               upload_form=form,
                               generator_form=get_generator_form())


@app.route('/generate', methods=['POST'])
def generate():
    ids = request.form.getlist('data_set')
    if len(ids) == 0:
        flash('Select at least one data set to start generation', 'error')
        return redirect(url_for('index'))

    m = MarkovGenerator(2)
    items = list()
    for data_set in ids:
        res = Resource.query.get(data_set)
        path = text_files.path(res.filename)
        m.learn(file(path).read())

    while len(items) < 10:
        sentence = m.say()
        if len(sentence.split(' ')) > 4:
            items.append(sentence)

    return render_template('generate.html', items=items)
