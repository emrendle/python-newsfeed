from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
# engine manages the overall connection to the db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# session generates temporary connections for performing CRUD operations
Session = sessionmaker(bind=engine)
# base helps us map the models to the real mysql tables
Base = declarative_base()