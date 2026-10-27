import uuid
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY, UUID as PGUUID

from datetime import datetime
from enum import Enum
from decimal import Decimal

class ProductsTypes(str,Enum):
    item = "item"
    subscription = "subscription"
    cosmetic = "cosmetic"
    non_listed = "non_listed"

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    username: str
    nick: str
    email: str
    hashed_password: str
    favorites: list[uuid.UUID] = Field(default=[], sa_column=Column(ARRAY(PGUUID(as_uuid=True))))

    servers: list["Server"] = Relationship(back_populates="owner")
    acquisitions: list["Acquisition"] = Relationship(back_populates="user")

class Server(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    id_owner: uuid.UUID = Field(foreign_key="user.id")

    name: str
    descrition: str
    url_icon: str
    server_ip: str
    server_port: int
    rcon_port: int
    hashed_rcon_password: str

    owner: User = Relationship(back_populates="servers")
    products: list["Product"] = Relationship(back_populates="server")

class Acquisition(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    id_product: uuid.UUID = Field(foreign_key="product.id")
    id_user: uuid.UUID = Field(foreign_key="user.id")

    purchase_date: datetime = Field(default_factory=datetime.utcnow)
    expiration_date: datetime | None = Field(default=None)

    product: "Product" = Relationship(back_populates="acquisitions")
    user: User = Relationship(back_populates="acquisitions")

class Product(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    id_server: uuid.UUID = Field(foreign_key="server.id")

    type: ProductsTypes
    name: str
    descrition: str
    url_icon: str
    price: Decimal = Field(default=0.00, max_digits=10, decimal_places=2)
    command: str
    validity_days: int | None = Field(default=None)

    server: Server = Relationship(back_populates="products")
    acquisitions: list["Acquisition"] = Relationship(back_populates="product")
