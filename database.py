from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#MySQL URL
DATABASE_URL = "mysql+pymysql://root:Meignana@localhost/customer"

#Create Engine
engine = create_engine(DATABASE_URL)

#Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Base Class
Base = declarative_base()
