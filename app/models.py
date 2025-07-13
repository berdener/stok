
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Urun(Base):
    __tablename__ = "urunler"
    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String)
    numara_araligi = Column(String)
    stok = Column(Integer)
    varyant = Column(String)
