# FastAPI uses SQL-Alchemy which uses in memory SQLite Database by implementing ORM.

# ORM: Object Relational Mapping, It basically maps Objects to Database Fields
# Example: We have a table 'pets' and we create a Class 'Pet',
#          So now this Class is reponsible for the crud part of the table.
#          Hence mapping b/w 'pets' and 'Pet'

from sqlalchemy import create_engine # To create Engine
from sqlalchemy.ext.declarative import declarative_base # To declare a Mapping
from sqlalchemy.orm import sessionmaker # To Create a Session

# Step-1 : Create an Engine

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' # It sets the URL for the database you want to connect to. In this case, it's using the SQLite database, which is a file-based database

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# connect_args={'check_same_thread': False}: 

# This is an additional argument passed to the create_engine function. 
# For SQLite databases, this argument is used to indicate that connections can be used across multiple threads. 
# In SQLite, by default, connections are not thread-safe, but setting check_same_thread to False allows them to be used in a multi-threaded environment.

# Step-2 : Declare a Mapping

Base = declarative_base()

# Step-3 : Create a Session

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# bind=engine       : The Session we created will bind the Engine named 'engine'
# autocommit=False  : The changes made within a session are not automatically committed to the database. 
#                     You'll have to explicitly call session.commit() to persist the changes. 
# autoflush=False   : changes made within a session are not automatically flushed to the database. 
#                     This means that you have more control over when data is actually written to the database.




