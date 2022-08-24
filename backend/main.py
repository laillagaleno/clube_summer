# from uuid import uuid4
# from pydantic import BaseModel

from typing import Union
import sys

from fastapi import FastAPI
sys.path.insert(0, '/home/laillagaleno/Projetos/React/clubesummer/backend')

app = FastAPI()
from app.sql_app.main import *


@app.get("/")
def read_root():
    # print("Hello")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

