from fastapi.testclient import TestClient
from ..main import app
from ..dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection_string = "postgresql://postgres:admin@localhost:5432/postgres"

engine = create_engine(connection_string, pool_size=3, max_overflow=0)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
