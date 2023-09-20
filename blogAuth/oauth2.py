from fastapi import Depends, HTTPException, status

from jose import JWTError, jwt

from .schemas import TokenData

from . import token 

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token') # So this is basically the route, from where fastapi will fetch token

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Toekn verification using function defined in token.py
    return token.verify_token(data, credentials_exception)

# Now, head over to '/blog' route and authenticate.
