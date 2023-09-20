# Our intended task is to refactor this main.py using routers

# Moving 'blog' route endpoints to 'blog.py'
# Moving 'user' related endpoints to 'user.py'
# Moving 'get_db()' to 'database.py'

from fastapi import FastAPI

from . import models
from .database import engine

from .routers import blog
from .routers import user

models.Base.metadata.create_all(engine) 
app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)


