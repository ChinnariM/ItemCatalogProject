import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
	#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           
           'id'         : self.id,
           'name'         : self.name,
           'email'         : self.email		   
       }

 
class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
	#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           
           'id'         : self.id,
           'name'         : self.name
       }
 
class Items(Base):
    __tablename__ = 'items'


    title = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category) 
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           'title'         : self.title,
           'description'         : self.description,
           'id'         : self.id           
       }
 

engine = create_engine('sqlite:///catalog.db')
 

Base.metadata.create_all(engine)