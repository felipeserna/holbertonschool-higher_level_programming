#!/usr/bin/python3
"""
Module - prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
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

    user_filter = sys.argv[4]

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    filter_a = State.name.like(func.binary('{}'.format(user_filter)))
    rows = session.query(State).filter(filter_a).all()

    if not rows:
        print("Not found")
    for row in rows:
        print("{}".format(row.id))

    session.close()
