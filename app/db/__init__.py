from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# global variable - flask creates a new contect every time a server request is made, these context provide global variables that can be shared across modules as long as the context is still active
from flask import g

load_dotenv()

# connect to database using env variable
# engine manages the overall connection to the db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# session generates temporary connections for performing CRUD operations
Session = sessionmaker(bind=engine)
# base helps us map the models to the real mysql tables
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db)

# whenever this function is called it returns a new session-connection object 
# allows us to perform additional logic before creating the db connection
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db

# finds and removes db from the g object
def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()