#!/usr/bin/python3
"""prints the State object with the name passed as argument
"""

import sys
from model_state import Base, State

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

    cont = session.query(State).filter_by(name=sys.argv[4]).count()

    if cont == 0:
        print("Not found")
    else:
        for state in session.query(State).filter_by(name=sys.argv[4]):
            print("{}".format(state.id))

    session.close()
