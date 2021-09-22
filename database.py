import sqlalchemy

connection_string = "mssql+pyodbc://\
    socoroadmin@socoro:$0c0r0-00@socoro.database.windows.net:1433/\
    SocoroDEV?driver=ODBC+Driver+17+for+SQL+Server"
engine = sqlalchemy.engine.create_engine(connection_string)
engine.connect()
