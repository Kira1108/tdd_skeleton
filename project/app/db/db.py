import logging
logger = logging.getLogger()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root:root123@localhost:5306"
DATABASE_NAME = "text_summary"

Base = declarative_base()

def create_database():
    engine = create_engine(DATABASE_URL)

    # create database
    with engine.connect() as conn:
        conn.execute(f"create database if not exists {DATABASE_NAME} ;")
        
# create database
create_database()

# engine with database 
engine = create_engine(f"{DATABASE_URL}/{DATABASE_NAME}")
Session = sessionmaker(bind=engine)
db = Session()

def init_db():
    logger.info("Initializing Database")
    Base.metadata.create_all(engine)
    logger.info("Database Initialized")


