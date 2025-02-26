from fastapi import FastAPI

from fastapi_version.routers import item_router

app = FastAPI()

app.include_router(item_router.router)
