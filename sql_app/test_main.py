from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import Base

from .main import app, get_db

SQLALCHEMY_DATABASE_URL = "mysql://root@localhost/bhinneka_dbms"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_main():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"msg": "Welcome"}

def test_read_users():
	response = client.get("users/1")
	assert response.status_code == 200
	assert response.json() == {"email": "sultan.emoticons@gmail.com",
	"id_pelanggan": 1,
	"status_pengiriman": []
	}	

def test_read_item():
	response = client.get("items/10")
	assert response.status_code == 200
	assert response.json() == {"status_pengiriman": "Belum Terkirim",
	"barang_diterima": "Belum Diterima",
	"id_transaksi": 10,
	"id_pelanggan": 1
	}	

def test_create_user():
	response = client.post(
		"/users/",
		json={"email": "deadpoodls@gmail.com", "password": "password"},
	)
	assert response.status_code == 200, response.text
	data = response.json()
	assert data["email"] == "deadpoodls@gmail.com"
	assert "id_pelanggan" in data
	user_id = data["id_pelanggan"]

	response = client.get(f"/users/{user_id}")
	assert response.status_code == 200, response.text
	data = response.json()
	assert data["email"] == "deadpoodls@gmail.com"
	assert data["id_pelanggan"] == user_id

def test_create_item_for_user():
	response = client.post(
		"/users/2/items/",
		json={"id_pelanggan": 2, "status_pengiriman": "Belum Dikirim", "barang_diterima": "Belum Diterima", "id_pembayaran" : 2},
	)

	assert response.status_code == 200, response.text

