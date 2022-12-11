from models import User
import schemas
import uuid


async def get_all_users() -> list[User]:
    return User.objects


async def create_user(user: schemas.PostUser) -> User:
    new_user = User(
        user_id=uuid.uuid4(),
        name=user.name,
        login=user.login,
        password=user.password,
    ).save()
    return new_user


async def delete_user(user_id):
    for user in User.objects:
        if user.user_id == user_id:
            user.delete()
            return


async def update_user(user_id, user_post: schemas.PostUser) -> User:
    for user in User.objects:
        if user.user_id == user_id:
            user.name = user_post.name
            user.login = user_post.login
            user.password = user_post.password
            user.save()
            return user
