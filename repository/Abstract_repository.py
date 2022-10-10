import abc
import os 

from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

class AbstractRepository(abc.ABC):
    engine = create_engine(os.environ.get('DATABASE_URL'))
    Base.metadata.create_all(engine, checkfirst = True)
    Session = scoped_session(sessionmaker(bind = engine))
    session = Session()
