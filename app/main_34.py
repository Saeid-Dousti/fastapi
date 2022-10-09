'''
    minute 8:34, get user info via owner_id 
'''

from ctypes import util
import time

# from pydantic import BaseModel #
from random import randrange
from typing import List, Optional
from webbrowser import get
from importlib_metadata import Deprecated  

import psycopg2
from certifi import contents
# from  passlib.context import CryptContext # moved to utils

# from fastapi import FastAPI, Response # to get status code
# from fastapi import FastAPI, Response, status # to get status code
# from fastapi import (  # to get status code
#     Depends,
#     FastAPI,
#     HTTPException,
#     Response,
#     status,
# ) 
from fastapi import FastAPI #
from fastapi.params import Body
from psycopg2.extras import (
    RealDictCursor,  # just to make sure returned query includes column name as well
)
# from sqlalchemy.orm import Session

# from . import models, schemas, utils #
from . import models
# from .database import engine, SessionLocal #
from .database import engine, get_db #
from .routers import post_34, user_32, auth_31 #* 8:34


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # moved to utils
models.Base.metadata.create_all(
    bind=engine
)  # This creats all the tables if it does not exist already and
# if it does it won't touch it to include modifications based on models file!

app = FastAPI()

app.include_router(post_34.router) #* 8:34
app.include_router(user_32.router) #
app.include_router(auth_31.router) #*


####################################


@app.get("/")
def root():
    return {"message": "Hello World"}
