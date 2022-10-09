'''
    minute 8:41, 
'''
from fastapi import FastAPI #

# from . import models, schemas, utils #
from . import models
# from .database import engine, SessionLocal #
from .database import engine
from .routers import post_35, user_32, auth_31 #* 8:41


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # moved to utils
models.Base.metadata.create_all(
    bind=engine
)  # This creats all the tables if it does not exist already and
# if it does it won't touch it to include modifications based on models file!

app = FastAPI()

app.include_router(post_35.router) #* 8:41 query paramenters
app.include_router(user_32.router) #
app.include_router(auth_31.router) #*


####################################


@app.get("/")
def root():
    return {"message": "Hello World"}
