#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # filter tables cities and states
    query = session.query(State, City).join(State, State.id ==
                                            City.state_id).order_by(City.id)
    for _states, _cities in query.all():
        print("{}: ({}) {}".format(_states.name, _cities.id, _cities.name))

    session.close()
