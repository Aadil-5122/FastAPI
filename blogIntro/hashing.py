# For password Hashing

from passlib.context import CryptContext 

# Chosen arbitrary names for class and function

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

# It sets up a CryptContext object configured to use the bcrypt hashing algorithm for securely hashing and verifying passwords. 
# It also has automatic handling for deprecated hashing algorithms.

class Hash():

    def bcrypt(password: str):
        return pwd_cxt.hash(password)
