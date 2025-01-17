basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# Models and relationships

class Dataset(db.Model):
    __tablename__="datasets"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(250), nullable=False)
    DOI = db.Column(db.String(250))   
    authors=db.relationship("Author",backref="datasets")
    def __repr__(self):
        return f'<Dataset: "{self.title}">'
    
class Author(db.Model):
    __tablename__="authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    orcid = db.Column(db.String(19), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.name
    

# CRUD operations

#### CREATE
@app.route('/author/create/', methods=['POST'])
def create():
    request_data = request.get_json()

   # if request_data:
        if 'name' in request_data:
            name = request_data['name']

        if 'orcid' in request_data:
            orcid = request_data['orcid']
    
    anauthor = Author(name=name,orcid=orcid)
    db.session.add(anauthor)
    db.session.commit()
    
    return '''
           Author {} registered in DB with {} orcid'''.format(name, orcid)