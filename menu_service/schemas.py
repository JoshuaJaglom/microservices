from pydantic import BaseModel


class PostMenu(BaseModel):
    product: str
    price: int


class Menu(PostMenu):
    id: int

# class PostProduct(BaseModel):
#     name: str
#     price: int
#     description: str
#
#
# class Product(PostProduct):
#     id: int
