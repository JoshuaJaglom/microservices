import mongoengine
from fastapi import FastAPI
from router import router
from fastapi.middleware.cors import CORSMiddleware

DB_NAME = 'mydb'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    mongoengine.connect(host=f"mongodb://mongo_users:27017/{DB_NAME}", alias=DB_NAME)


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


app.include_router(router, prefix='/v1')
