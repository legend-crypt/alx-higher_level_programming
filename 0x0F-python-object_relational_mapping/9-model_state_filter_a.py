#!/usr/bin/python3

"""
    Write a script that lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base

    engine = create_engine(
        """mysql+mysqldb://{}:{}@localhost/{}""".format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
        )
    Session = sessionmaker()
    session = Session(bind=engine)
    columns = session.query(State).filter(State.name.like('%a%'))
    for row in columns:
        print("{}: {}".format(row.id, row.name))
