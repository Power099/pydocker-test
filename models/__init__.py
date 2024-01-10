from .db import Base, engine
from .user import *

Base.metadata.create_all(bind=engine)
