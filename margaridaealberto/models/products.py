from email.policy import default
from teresaefrancisco import model 
from teresaefrancisco.sql_db import db
from sqlalchemy import Column, Integer , String , Text ,Float , Boolean
from sqlalchemy.orm import relationship

class Product(db.Model ,model.Model,model.Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(Text)
    price = Column(Float)
    price_paid = Column(Float, default= 0.0)
    store = Column(Text)
    show_price = Column(Boolean, default=True)
    priority = Column(Integer, default=10)

    images = relationship('ProductImage', back_populates="product")
    contributions = relationship('Contribution', back_populates="product")

    def calculate_percentage(self):
        if self.price:
            ratio = (self.price_paid/self.price)
            return ratio * 100 if ratio <=1 else 100
        else:
            return 0.0

    def missing_value(self):
        return self.price - self.price_paid if self.price >= self.price_paid else 0

    def is_paid(self):
        return False if self.missing_value()>0 else True

    def update_price_paid(self):
        price_paid = sum([contribution.value_contributed for contribution in self.contributions])
        self.price_paid = price_paid
        self.save()

    def update_with_dict(self,values):
        if values['name'] and values['name'] != self.name:
            self.name = values['name']
        if values['description'] and values['description'] != self.description:
            self.description = values['description']
        if values['price'] and values['price'] != self.price:
            self.price = values['price']
        if values['store'] and values['store'] != self.store:
            self.store = values['store']
        if values['show_price'] != self.show_price:
            self.show_price = values['show_price']
        self.save()
        return True