import schemas
import models


def mapping_model_schema(model: models.User):
    schema = schemas.User(
        user_id=model.user_id,
        name=model.name,
        login=model.login,
        password=model.password,
    )
    return schema


def mapping_schema_model(schema: schemas.User):
    model = schemas.User(
        user_id=schema.user_id,
        name=schema.name,
        login=schema.login,
        password=schema.password,
    )
    return model
