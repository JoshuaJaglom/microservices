import uuid

from fastapi import APIRouter, status

import mapper
import user_service
from schemas import User, PostUser

router = APIRouter(
    tags=['User'],
    prefix='/users',
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[User])
async def get_all_users():
    users = await user_service.get_all_users()
    result = [
        mapper.mapping_model_schema(user)
        for user in users
    ]
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=User)
async def add_new_user(user: PostUser):
    new_user = await user_service.create_user(user)
    return new_user


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: uuid.UUID):
    await user_service.delete_user(user_id)
    return


@router.put('/{user_id}', status_code=status.HTTP_202_ACCEPTED, response_model=User)
async def update_user(user_id: uuid.UUID, user_post: PostUser):
    upd_user = await user_service.update_user(user_id, user_post)
    result = mapper.mapping_model_schema(upd_user)
    return result

