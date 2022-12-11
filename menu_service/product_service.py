from models import Product
import schemas
import uuid


async def get_all_products() -> list[Product]:
    return Product.objects


async def create_product(product: schemas.PostProduct) -> Product:
    new_product = Product(
        product_id=uuid.uuid4(),
        product=product.product,
        price=product.price,
    ).save()
    return new_product


async def delete_product(product_id):
    for product in Product.objects:
        if product.product_id == product_id:
            product.delete()
            return

