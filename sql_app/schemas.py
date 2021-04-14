from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):

    status_pengiriman: str

    barang_diterima: Optional[str] = None

class ItemCreate(ItemBase):

    pass

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
