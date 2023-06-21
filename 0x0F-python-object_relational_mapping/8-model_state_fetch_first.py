#!/usr/bin/python3

"""
    Write a script that prints the first State object
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv
    try:
        engine = create_engine(
            """mysql+mysqldb://{}:{}@localhost/{}""".format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True
        )
    except Exception as e:
        print(e)
    Session = sessionmaker()
    session = Session(bind=engine)
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print()
