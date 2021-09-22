from fastapi import FastAPI

app = FastAPI()

import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};\
    Server=tcp:socoro.database.windows.net,1433;\
    Database=SocoroDEV;\
    Uid=socoroadmin;Pwd=$0c0r0-00;\
    Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
cursor = conn.cursor()
cursor.execute("select * from Operations")
row = cursor.fetchone()

if row:
    print(row)
