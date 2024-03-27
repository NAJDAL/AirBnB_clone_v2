#!/usr/bin/python3
"""This module defines the DBStorage class for AirBnB."""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from os import environ


class DBStorage:
    """Storage for database with SQL Alchemy and MySQL."""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor."""
        sql_user = environ.get('HBNB_MYSQL_USER')
        sql_pwd = environ.get('HBNB_MYSQL_PWD')
        sql_host = environ.get('HBNB_MYSQL_HOST')
        sql_db = environ.get('HBNB_MYSQL_DB')
        sql_env = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sql_user, sql_pwd, sql_host, sql_db),
                                      pool_pre_ping=True)

        if sql_env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        session = self.__session
        obj_dict = {}
        if not cls:
            tables = [User, State, City, Amenity, Place, Review]
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            tables = [cls]

        for table in tables:
            query = session.query(table).all()

            for row in query:
                key = "{}.{}".format(type(row).__name__, row.id)
                obj_dict[key] = row

        return obj_dict

    def new(self, obj):
        """Add the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        and creates the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes Session."""
        self.__session.close()

