# For password Hashing

from ctypes.wintypes import PDWORD
from pydoc import plain
from passlib.context import CryptContext 

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():

    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    # Password Verification
    def verify(hashed_password, plain_password):
         return pwd_cxt.verify(plain_password, hashed_password)
