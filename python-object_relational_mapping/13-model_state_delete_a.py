#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), echo=True)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # delete records
    query = session.query(State).filter(State.name.like('%a%'))
    for deleted_rec in query.all():
        session.delete(deleted_rec)
    session.commit()

    session.close()
