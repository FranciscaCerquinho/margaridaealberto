from teresaefrancisco import model 
from teresaefrancisco.sql_db import db
from sqlalchemy import Column, Integer , Text , Boolean

class Confirmation(db.Model ,model.Model,model.Base):
    __tablename__ = 'confirmation'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    has_food_restriction = Column(Boolean)
    food_restriction = Column(Text)
    is_vegetarian = Column(Boolean)
    comment = Column(Text)
