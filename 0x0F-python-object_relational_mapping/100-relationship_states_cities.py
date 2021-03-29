#!/usr/bin/python3
""" I'm going to be mad """

if __name__ == "__main__":
    import sqlalchemy
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import Base, City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    add_s = State(name="California")
    add_s.cities = [City(name="San Francisco")]

    session.add(add_s)

    session.commit()

    session.close()
