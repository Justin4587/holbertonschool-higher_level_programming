#!/usr/bin/python3
""" I'm going to be mad """

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))

    session.commit()

    session.close()
