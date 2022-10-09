'''
    minute 10:30, alembic, alembic.env.py and alembic.ini
    minute 11:14, remove  
'''
from fastapi import FastAPI #
from fastapi.middleware.cors import CORSMiddleware #* 11:19

# from . import models, schemas, utils #
from . import models
# from .database import engine, SessionLocal #
from .database import engine
from .routers import vote_36, post_37, user_32, auth_31 #* 8:41
from .config import settings 

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # moved to utils

# models.Base.metadata.create_all(bind=engine)  #* 11:14 commenting this # This creats all the tables if it does not exist already and

# if it does it won't touch it to include modifications based on models file!

app = FastAPI()

origins = ["https://www.google.com"] #* 11:20 alowing google domail to talk to us
# origins = ["*"] #* 11:20 making it public

app.add_middleware( #* 11:20
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_37.router) # 10:15 join
app.include_router(user_32.router) #
app.include_router(auth_31.router) #
app.include_router(vote_36.router) #


####################################


@app.get("/")
def root():
    return {"message": "Hello World"}
