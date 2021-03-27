#!/usr/bin/python3
""" I'm going to be mad """

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = session.query(State).filter_by(name='Texas').first()
        print("{}".format(states.id))
    except:
        print("Not Found")

    session.close()
