from fastapi import FastAPI, Depends
from .routers import operation
from.dependencies import get_db

app = FastAPI()
app.include_router(operation.router)
