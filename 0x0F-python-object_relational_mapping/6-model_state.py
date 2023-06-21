#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    #Base.metadata.create_all(engine)
    
    # state1 = State(name="California")
    # state2 = State(name="Arizona")
    # state3 = State(name="Texas")
    # state4 = State(name="New York")
    # state5 = State(name="Nevada")
    
    # states = [state1, state2, state3, state4, state5]
    # Session = sessionmaker(bind=engine)
    # session = Session()
    
    # for state in states:
    #     session.add(state)
    # session.commit()
    