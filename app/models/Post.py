from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  # defining foreign key that references users table
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  user = relationship('User')
  # on delete cascade will delete the corresponding foreign key records when a record from the specified table is deleted.
  # deleting a post from the db will delete all its associated comments  
  comments = relationship('Comment', cascade='all,delete')
  # when we query the model, this property will perform a SELECT, paired with the SQLAlchemy func.count() it will add up the votes    
  vote_count = column_property(
  select([func.count(Vote.id)]).where(Vote.post_id == id)
  )
  # all votes get deleted when a post is deleted   
  votes = relationship('Vote', cascade='all,delete')

# querying a post will return 1- the post 2- the comments and 3- the user who left the comment (as defined in the comment model)