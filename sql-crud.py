from sqlalchemy import(
    create_engine, Integer, Column, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instroction from 'chinook' databse
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based modal for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connceting to the database directly, we will ask for a session
# create a new instance of session maker, then point to our engine (the db)
Session = sessionmaker(db)

#open an actual session by callung the session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)


#Creating records on our programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

# Add each instance of our programmers to our session
session.add(ada_lovelace)

# Commit our session to the database
session.commit()

#query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + "" + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
        )