# Head over to '/docs' endpoint to see all the endpoints hosted using Swagger UI

from fastapi import FastAPI

app = FastAPI() # Created the instance of FastAPI

# To establish FastAPI working, we decorate a function as in Line 10: 
# "app" is the name of the created instance, 
# "get" is the type of request, 
# "('/')" specifies the URL Path that would execute the function below it.

@app.get('/') 
def index():
    return "heyy"   # Returning a normal String at the default endpoint '/'

@app.get('/about')
def about():
    return {'data':{'name':'findr'}}    # Returning a JSON Formatted Text (Dictionary) at the endpoint '/about'