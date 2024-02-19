#!/usr/bin/python3

"""Creates City table and list the cities in the database"""
from model_state import State, Base
from sqlalchemy import (
    create_engine, Integer,
    String, Column, ForeignKey
)
from sqlalchemy.orm import sessionmaker
from sys import argv, exit


class City(Base):
    """Creates the city table"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)


if __name__ == "__main__":
    if len(argv) < 4:
        print("Input DbUser, Dbpassword and Dbname")
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2],
                                  argv[3],
                                  pool_pre_ping=True))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name,
                          City.id,
                          City.name).join(City).order_by(
                              City.id).all()
    for state_name, city_id, city_name in query:
        print(f"{state_name}: ({city_id}) {city_name}")
