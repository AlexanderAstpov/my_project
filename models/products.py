
from database.db import Base
from sqlalchemy import Column, Integer, String



class Product(Base):
    __tablename__= "goods"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    article = Column(Integer, nullable=False)
    color = Column(String, nullable=True)
    len = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    link_1 = Column(String, nullable=True)
    link_2 = Column(String, nullable=True)
    link_3 = Column(String, nullable=True)
    link_4 = Column(String, nullable=True)

    
    # count = Column(Integer, default=0)