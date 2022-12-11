from fastapi import APIRouter, status
from schemas import Menu, PostMenu
from create_menu import generate_menu

router = APIRouter(
    tags=['Menu'],
    prefix='/menu',
)

serial = 5
menu = generate_menu(serial)


@router.get('/', status_code=200, response_model=list[Menu])
async def get_menu():
    return menu


# Don't work with '/', redirect error
@router.post('/add', status_code=201, response_model=Menu)
async def add_position_menu(post_menu: PostMenu):
    global serial
    new_menu = Menu(
        id=serial,
        product=post_menu.product,
        price=post_menu.price,
    )
    serial += 1
    menu.append(new_menu)
    return new_menu


@router.delete('/{menu_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu(menu_id: int):
    for i, position in enumerate(menu):
        if position.id == menu_id:
            menu.pop(i)
            return
