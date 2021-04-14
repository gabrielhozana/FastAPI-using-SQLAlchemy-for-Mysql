from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):

    __tablename__ = "pelanggan"


    id_pelanggan = Column(Integer, primary_key=True, index=True)
    nama_pelanggan = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    items = relationship("Item", back_populates="owner")



class Item(Base):

    __tablename__ = "transaksi"


    id_transaksi = Column(Integer, primary_key=True, index=True)
    status_pengiriman = Column(String, index=True)
    barang_diterima = Column(String, index=True)
    id_pelanggan = Column(Integer, ForeignKey("pelanggan.id_pelanggan"))

    owner = relationship("User", back_populates="items")
