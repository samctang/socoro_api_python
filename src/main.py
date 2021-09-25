from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.routers import operation

app = FastAPI()
app.include_router(operation.router)


@app.get("/")
async def redirect():
    response = RedirectResponse(url='/docs')
    return response
