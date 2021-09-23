from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection_string = "mssql+pyodbc://\
socoroadmin@socoro:$0c0r0-00@socoro.database.windows.net:1433/\
SocoroDEV?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
