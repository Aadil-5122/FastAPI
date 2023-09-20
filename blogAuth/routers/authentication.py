# To create a login system for users to access the endpoints.

from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm

from .. import token # To return JWT in case of Correct Credentials

router = APIRouter(
    tags=['Authentication']
)

# Remember to add this route to 'main.py' as well.

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    # Now, we need to verify the password as well:
    if Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')

    # We will generate a JWT Token if the credentials are correct, and return it

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Finally, we will be authenticating the API Routes.
# For that we have 'oauth2.py'