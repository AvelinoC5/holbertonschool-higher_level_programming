#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa
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

    # update record
    updated_rec = session.query(State).filter_by(id="2").first()
    updated_rec.name = "New Mexico"
    session.commit()

    session.close()
