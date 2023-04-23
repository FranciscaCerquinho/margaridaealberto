from teresaefrancisco import model 
from teresaefrancisco.sql_db import db
from sqlalchemy import Column, Integer , Text , JSON

class SpecificInfo(db.Model ,model.Model,model.Base):
    __tablename__ = 'specific_info'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    information = Column(JSON, nullable=True)
