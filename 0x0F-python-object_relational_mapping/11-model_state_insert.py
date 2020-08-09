#!/usr/bin/python3
"""
Module - adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    # persists data
    session.add(new_state)
    # confirm the change
    session.commit()
    rows = session.query(State).filter_by(name="Louisiana").all()
    print("{}".format(rows[0].id))

    session.close()
