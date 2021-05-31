from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):

    status_pengiriman: str = "Belum Dikirim"

    barang_diterima: Optional[str] = "Belum Diterima"

class ItemCreate(ItemBase):

    id_pembayaran: int

class Item(ItemBase):
    id_transaksi: int
    id_pelanggan: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):

    email: str

class UserCreate(UserBase):

    password: str

class User(UserBase):
    id_pelanggan: int
    status_pengiriman: List[Item] = []

    class Config:
        orm_mode = True
