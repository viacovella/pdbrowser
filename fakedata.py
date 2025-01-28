from app import db, Dataset, RepositoryEnum, Author
from datetime import datetime


db.drop_all()
db.create_all()

a1=Author(name="Arsenio Steele",email="cras.dictum@google.couk",orcid="6301-7818-5359-5100")
a2=Author(name="Dustin Hooper",email="nec.metus@hotmail.couk",orcid="8291-4553-6032-1668")
a3=Author(name="Jenna Hampton",email="nulla.eget.metus@icloud.ca",orcid="8697-4645-9456-3867")
a4=Author(name="Ashton Burton",email="dui.fusce@protonmail.net",orcid="2607-5424-8311-6240")

[db.session.add(a) for a in [a1,a2,a3,a4]]
db.session.commit()


d1=Dataset(timestamp=datetime(2022,12,23),title="Neural correlates of psychological manipulatons", DOI="doi.org/10.1023.12", Repository=RepositoryEnum.zenodo)
d2=Dataset(timestamp=datetime(2021,2,18),title="Psychological correlates of brain stimulations", DOI="doi.org/17.1231.5", Repository=RepositoryEnum.zenodo)
d3=Dataset(timestamp=datetime(2023,7,30),title="Social psychology dataset", DOI="doi.org/10.1234.5", Repository=RepositoryEnum.zenodo)

d1.authors.append(a1)
d2.authors.append(a1)
d1.authors.append(a2)

[db.session.add(d) for d in [d1,d2,d3]]
db.session.commit()