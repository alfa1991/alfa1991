# fastapi_app/main.py

from fastapi import FastAPI
from views import item_router

app = FastAPI()

app.include_router(item_router)

# Запустите приложение, используя uvicorn:
# uvicorn main:app --reload