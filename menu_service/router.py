import uuid

from fastapi import APIRouter, status

import mapper
import product_service
from schemas import Product, PostProduct


router = APIRouter(
    tags=['Menu'],
    prefix='/menu',
)


@router.get('/', status_code=200, response_model=list[Product])
async def get_product():
    products = await product_service.get_all_products()
    result = [
        mapper.mapping_model_schema(product)
        for product in products
    ]
    return result


@router.post('/add', status_code=201, response_model=Product)
async def add_product(post_product: PostProduct):
    new_user = await product_service.create_product(post_product)
    return new_user


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu(product_id: uuid.UUID):
    await product_service.delete_product(product_id)
    return
