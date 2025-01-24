from app import db, Dataset, RepositoryEnum
from datetime import datetime


db.drop_all()
db.create_all()

d1=Dataset(timestamp=datetime(2022,12,23),title="Neural correlates of psychological manipulatons", DOI="doi.org/10.1023.12", Repository=RepositoryEnum.zenodo)
d2=Dataset(timestamp=datetime(2021,2,18),title="Psychological correlates of brain stimulations", DOI="doi.org/17.1231.5", Repository=RepositoryEnum.zenodo)
d3=Dataset(timestamp=datetime(2023,7,30),title="Social psychology dataset", DOI="doi.org/10.1234.5", Repository=RepositoryEnum.zenodo)

[db.session.add(d) for d in [d1,d2,d3]]
db.session.commit()