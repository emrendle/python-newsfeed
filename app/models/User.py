from app.db import Base
from sqlalchemy import Column, Integer, String
# for validating data before adding into db
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

# user inherits form the Base class created in the app/db init.py
# we're declaring properties that the parent Base class will use to make the table
# the classes used to define the columns and data types come from sqlalchemy
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    # assert keyword automatically throws an error if the condition is false, which prevents the return statement from happening
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

    # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)