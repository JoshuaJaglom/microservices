from schemas import Menu


def generate_menu(number) -> list[Menu]:
    return [
        Menu(
            id=i,
            product=str(i),
            price=str(i)
        ) for i in range(number)
    ]
