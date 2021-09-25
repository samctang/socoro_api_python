from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection_string = "postgresql://lpuinnfdjtcjoy:ddef5874ab7d88bad04a1ae66895a18b4bce20591075c33d8790fcaec5e56811\
@ec2-34-233-187-36.compute-1.amazonaws.com:5432/d7n0lkjiq6p5m3"

engine = create_engine(connection_string, pool_size=3, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
