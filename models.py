from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Confession(Base):
	__tablename__ = 'confession'
	id = Column(Integer, primary_key=True)
	message = Column(String)
	hub = Column(String)


class Letter(Base):
  __tablename__ = 'letter'
  id = Column(Integer, primary_key=True)
  initials = Column(String)
  seclet = Column(String)
  