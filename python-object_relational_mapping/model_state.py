#!/usr/bin/python3
"""contains the class definition of a State and
an instance Base = declarative_base()"""


import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Create a declarative base instance
Base = declarative_base()


# Define the State class
class State(Base):
    __tablename__ = 'states'  # Link to the MySQL table states

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True
        )

    # Create the table(s) if not exists
    Base.metadata.create_all(engine)
