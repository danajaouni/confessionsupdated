from models import Base, Confession, Letter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_Confession(message, hub):
	confession_object = Confession(
    message=message,hub=hub)
	session.add(confession_object)
	session.commit()

def delete_Confession(id):
  session.query(Confession).filter_by(id = id).delete()
  session.commit()

def add_Letter(initials, seclet):
  letter_object = Letter(
    initials=initials,seclet=seclet)
  session.add(letter_object)
  session.commit()

def delete_Letter(id):
  session.query(Letter).filter_by(id = id).delete()
  session.commit()

