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

class RepositoryEnum(enum.Enum):
    zenodo = 'Zenodo'
    osf = 'OSF'
    openneuro = 'Open Neuro'

class Dataset(db.Model):



    __tablename__="datasets"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    title = db.Column(db.String(250), nullable=False)
    DOI = db.Column(db.String(250))
    Repository = db.Column(db.Enum(RepositoryEnum),default=RepositoryEnum.osf)
#    authors=db.relationship("Author",backref="datasets")
    def __repr__(self):
        return f'<Dataset: "{self.title}">'
    
#class Author(db.Model):
#    __tablename__="authors"
#    id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#   #email = db.Column(db.String(120), unique=True, nullable=False)
#    orcid = db.Column(db.String(19), unique=True, nullable=False)
#    def __repr__(self):
#        return '<User %r>' % self.name
    

# VIEWS

@app.route('/')
def index():
    ndsets = Dataset.query.count()
    datasets = Dataset.query.all()
    return render_template('index.html', ndsets=ndsets, datasets=datasets)