from fastapi import FastAPI
from .routers import operation


app = FastAPI()
app.include_router(operation.router)
