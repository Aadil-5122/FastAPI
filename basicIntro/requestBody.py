# Till now we were using 'get' requests, Now lets see how FastAPI handles 'post' requests

# Major Difference:

# GET: Parameters are appended to the URL in the form of a query string. 
#      This means that the data is visible in the URL, which can be a security concern if sensitive information is being sent.

# POST: Data is included in the body of the request, which is not visible in the URL. 
#       This makes it more secure for transmitting sensitive information.

from fastapi import FastAPI

from typing import Optional # This is used to pass optional function argument

from pydantic import BaseModel 
# Now whenever we create a class and extend 'BaseModel' by passing it as a parameter in class:
# We say that this very class is now a pydantic Model. We define its parameters within the class and 
# finally, we need to declare it as a Request Body.

app = FastAPI()

@app.get('/') 
def index():
    return {'data':'blog list'}

@app.get('/blog') 
def show(limit: int, published: bool, sort: Optional[str]):
    if published:
        return {'data': f'{limit} blogs published from the db'}
    else:
        return {'data': f'{limit} blogs NOT published from the db'}

# Demonstration of POST Request:
# Now, POST Request can't be sent though URL, and it resides in the Body, So how do we verify it ?
# Ans: Swagger UI has different endpoints hosted for both POST and GET Requests. 

class Blog(BaseModel): # extending BaseModel 
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog): # Here we define that the 'REQUEST BODY' is 'blog' of the type 'Blog'
    return {'data': f'Blog is created with the title as {blog.title}'}  # In this line, we are returning just the 'title' part of the request body.
    # We can return the whole request body by simply using  'return blog'