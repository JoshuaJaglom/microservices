import schemas
import models


def mapping_model_schema(model: models.Product):
    schema = schemas.Product(
        product_id=model.product_id,
        product=model.product,
        price=model.price,
    )
    return schema


def mapping_schema_model(schema: schemas.Product):
    model = schemas.Product(
        product_id=schema.product_id,
        product=schema.product,
        price=schema.price,
    )
    return model
