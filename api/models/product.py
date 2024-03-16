from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    address: str
    city: str
    zipcode: str
    country: str

class ShipAddress(Address):
    pass

class User(BaseModel):
    firstname: str
    lastname: Optional[str]
    email: str
    password: str

class Customer(User):
    membership: bool
    mobile: str
    rewards: int

class Product(BaseModel):
    id: int
    productName: str
    categoryId: int
    unitInStock: Optional[int]
    unitPrice: float

class Order(BaseModel):
    id: int
    reference: str
    customerId: int
    products: List[Product]
    amount: float
    orderDate: str
    shippedDate: Optional[str]
    shipAddress: ShipAddress

class Category(BaseModel):
    id: int
    categoryName: str
    description: str
    picture: Optional[str]