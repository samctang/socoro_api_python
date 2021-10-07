from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.routers import operation

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(operation.router)

origins = [
    "http://localhost",
    "http://localhost:3011",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def redirect():
    response = RedirectResponse(url='/docs')
    return response
