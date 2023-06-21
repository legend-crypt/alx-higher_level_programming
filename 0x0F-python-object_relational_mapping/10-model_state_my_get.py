#!/usr/bin/python3
"""
Write a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
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
    searched = argv[4]
    columns = session.query(State).filter(State.name == searched)
    if columns.count() == 0:
        print("Not found")
    else:
        for row in columns:
            print(row.id)
