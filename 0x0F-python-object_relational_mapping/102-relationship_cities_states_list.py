#!/usr/bin/python3
""" I'm going to be mad """

if __name__ == "__main__":
    import sqlalchemy
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all = session.query(City).order_by(City.id).all()

    for row in all:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))

    session.commit()

    session.close()
