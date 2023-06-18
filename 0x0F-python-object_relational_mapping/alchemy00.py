#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine, String, Column, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:lehjend419619@localhost:3306/ormtest", echo=True)
engine.connect()
print(engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(200))
    fullname = Column(String(50))
    nickname = Column(String(50))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name="mark", fullname="mark ansah", nickname="okay")
session.add(user1)
Session.commit()