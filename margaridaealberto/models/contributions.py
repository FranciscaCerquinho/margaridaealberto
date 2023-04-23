from teresaefrancisco import model 
from teresaefrancisco.sql_db import db
from sqlalchemy import Column, Integer , String , Text ,Float , ForeignKey
from sqlalchemy.orm import relationship

from teresaefrancisco.tools import specific_info

class Contribution(db.Model ,model.Model,model.Base):
    __tablename__ = 'contribution'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    value_contributed = Column(Float)
    message = Column(Text)
    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship('Product', back_populates="contributions")

    def thank_you_message(self):
        return specific_info.generate_ty_contribution_message(self.name)

    def update_with_dict(self,values):
        if values['name'] and values['name'] != self.name:
            self.name = values['name']
        if values['message'] and values['message'] != self.message:
            self.message = values['message']
        if values['value_contributed'] and values['value_contributed'] != self.value_contributed:
            self.value_contributed = values['value_contributed']
        if values['product'] and values['product'] != self.product:
            self.product = values['product']
        self.save()
        self.product.update_price_paid()
        return True
