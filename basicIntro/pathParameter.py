# Head over to '/docs' endpoint to see all the endpoints hosted using Swagger UI

from fastapi import FastAPI

app = FastAPI() # Created the instance of FastAPI

@app.get('/') 
def index():
    return {'data':'blog list'}  # Returning a normal String at the default endpoint '/'

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'list of all unpulished blogs'}

# Following is the representation of how we add 'dynamic variables' to the PATH / endpoint URL

@app.get('/blog/{id}') # i.e. we use parenthesis with 'id' to use it dynamically. Here 'id is called PATH Parameter
def show(id):   # i.e. we also accept 'id' as a parameter when we want to use it as a dynamic variable in the URL
    # To fetch blog with blog_id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int): # Now herein ihave specified the datatype of 'id', by default it was 'str'. Any datatype mismatch would throw an error
    # fetch comments for blog of id = id
    return {'data': {'1', '2'}}

# Now here's a catch:
#    If I had defined the 'unpublished' function after 'comments' function and passed a string in the URL then FastAPI would have thrown error.
#    It is for the simple reason that FastAPI reads the code line by line and hence if 'comments' function preceeded the 'unpublished' function,
#    FastAPI would read it first and due to 'comments' function's limitation to accept only integers, any string passed to it would throw an error.

# Therefore, we need be careful in deciding the order of function definitions.