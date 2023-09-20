from fastapi import FastAPI

from typing import Optional # This is used to pass optional function argument

app = FastAPI()

@app.get('/') 
def index():
    return {'data':'blog list'}

# Demonstration: Using 'Query Parameters'

# Example 1 of hard-coded function decorator: @app.get('/blog?limit=50')
# Herein, query parameter is 'limit', its value is '50' 

@app.get('/blogging') 
def show(limit):   # Also we have to pass Query Parameter as a Function Argument to use it from URL.
    return {'data': f'{limit} blogs from the db'}

# Example 2 of hard-coded fucntion decorator: @app.get('/blog?limit=50&published=true')
# Herein, we have passed multiple query parameters using '&'
# Note: For 'published', we need to specify its datatype if have have 2 separate execution workflows for true and false,
#       because, default, which is string, would throw an error.

@app.get('/blogger') 
def show(limit, published: bool):   # Also we have to pass Query Parameter as a Function Argument to use it from URL.
    if published:
        return {'data': f'{limit} blogs published from the db'}
    else:
        return {'data': f'{limit} blogs NOT published from the db'}

# Example 3: We can also pass an Optional Query Parameter as the following Function

@app.get('/blog') 
def show(limit: int, published: bool, sort: Optional[str]): # 'sort' is an Optional Parameter of type 'str'
    if published:
        return {'data': f'{limit} blogs published from the db'}
    else:
        return {'data': f'{limit} blogs NOT published from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'list of all unpulished blogs'}

@app.get('/blog/{id}') 
def show(id):   
    # To fetch blog with blog_id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int): 
    # fetch comments for blog of id = id
    return {'data': {'1', '2'}}

# Note: The judging parameter for FastAPI as to, if the argument is a 'path' parameter or a 'query' parameter is;
#       if the PATH of Decorator has a variable in parenthesis, and the same is passed as a function argument, then 
#       that parameter is treated as a PATH Parameter, and Query Parameter Otherwise.
