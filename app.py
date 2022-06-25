from fastapi import FastAPI
from routes.task import task
from routes.user import user

app = FastAPI()

app.include_router(task)
app.include_router(user)