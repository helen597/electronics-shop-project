class Item:
    """
    Класс для представления товара в магазине.
    """
    # уровень цен с учетом скидки
    pay_rate = 1.0
    # список созданных экземпляров класса
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(float(price), float):
            raise ValueError('Цена должна быть числом')
        elif float(price) < 0:
            raise ValueError('Число должно быть неотрицательным')
        if not isinstance(quantity, int):
            raise ValueError('Количество должно быть целым числом')
        elif quantity < 0:
            raise ValueError('Число должно быть неотрицательным')
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        Item.all.append(self)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
