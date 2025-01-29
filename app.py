from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import enum

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# Models and relationships
# see also https://dev.to/jimgrimes86/flask-sqlalchemy-many-to-many-relationships-association-tables-and-association-objects-3aej

class RepositoryEnum(enum.Enum):
    zenodo = 'Zenodo'
    osf = 'OSF'
    openneuro = 'Open Neuro'

authorship = db.Table('dataset_author',
                    db.Column('dataset_id', db.Integer, db.ForeignKey('datasets.id')),
                    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'))
                    )


class Dataset(db.Model):
    __tablename__="datasets"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    title = db.Column(db.String(250), nullable=False)
    DOI = db.Column(db.String(250))
    Repository = db.Column(db.Enum(RepositoryEnum),default=RepositoryEnum.osf)
    authors=db.relationship("Author", secondary=authorship, back_populates="datasets")
    def __repr__(self):
        return f'<Dataset: "{self.title}">'
    
class Author(db.Model):
    __tablename__="authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    orcid = db.Column(db.String(19), unique=True, nullable=False)
    datasets = db.relationship("Dataset", secondary=authorship, back_populates="authors")
    def __repr__(self):
        return '<User %r>' % self.name



# VIEWS

@app.route('/')
def index():
    ndsets = Dataset.query.count()
    datasets = Dataset.query.all()
    return render_template('index.html', ndsets=ndsets, datasets=datasets)


@app.route('/author/<int:author_id>/')
def author(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author.html', author=author)

@app.route('/author/create/', methods=['POST'])
def acreate():
    request_data = request.get_json()

       
    if request_data:
        aname=request_data['name']
        aemail=request_data['email']
        aorcid=request_data['orcid']

    aauthor = Authos(name=aname,email=aemail,orcid=aorcid)
    db.session.add(aauthor)
    db.session.commit()
    
    return '''
           Created author:{} sent in a submission with orcid {}'''.format(aname,aorcid)