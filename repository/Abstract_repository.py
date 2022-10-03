import abc
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base


class AbstractRepository(abc.ABC):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Coders_1",
        database="db_lifechat"
    )

    engine = create_engine('mysql://root:Coders_1@localhost:3306/db_lifechat')
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # def get(self, entity_id):
    #     raise NotImplementedError

    def list(self):
        raise NotImplementedError