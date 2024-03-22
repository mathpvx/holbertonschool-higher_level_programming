#!/usr/bin/python3
"""
Script that lists all State objects from the specified database where the name contains 'a'.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Main function to retrieve and print State objects from the specified database.
    """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    states_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
    )

    for states in states_a:
        print("{}: {}".format(states.id, states.name))
    session.close()
