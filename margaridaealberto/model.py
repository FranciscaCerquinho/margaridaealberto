from .sql_db import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text

Base = declarative_base()

class Model():

    _name = None
    _description = None
    __tablename__ = None

    def __repr__(self):
        return '<User %r>' % self.username

    def create(self):
        db.session.add(self)
        db.session.commit()
        return True

    def save(self):
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def get_table(self,model):
        return db.session.query(self.table_object(table_name=model))

    def get_tables(self):
        tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}
        return tables_dict
    
    def table_object(self,table_name):
        tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}
        return tables_dict.get(table_name)
    
    def get_columns(self):
        return [column.key for column in self.__table__.columns]

    def get_columns_names_types(self):
        columns = self.__table__.c
        dict = {}
        for c in columns:
            dict[c.name] = c.type
        return dict
    
    def get_columns_names_types_from_name(self,table_name):
        columns = self.table_object(self,table_name).__table__.c
        dict = {}
        for c in columns:
            dict[c.name] = c.type
        return dict

    def add_to_session(self):
        db.session.add(self)
        db.session.commit()
        return True
    
    def refresh(self):
        db.session.refresh(self)
        return True

    def get_table(self,model):
        return db.session.query(self.table_object(table_name=model))

    def table_object(self,table_name):
        tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}
        return tables_dict.get(table_name)

    def all_tables_object(self):
        return {table.__tablename__: table for table in db.Model.__subclasses__()}

    def get_all_tables(self):
        return {table.__tablename__: db.session.query(table) for table in db.Model.__subclasses__()}