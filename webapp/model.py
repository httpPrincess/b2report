from webapp import db


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return '<Resource %r>' % self.id
