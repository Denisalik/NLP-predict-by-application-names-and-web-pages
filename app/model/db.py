from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = '188.130.155.81'
PORT = '15432'
USER = 'postgres'
PASS = '1nn0M3tr1c5_2022'
DATABASE = 'postgres'
URL = f'postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
