from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = ''
PORT = ''
USER = ''
PASS = ''
DATABASE = ''
URL = f'postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
