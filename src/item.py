import csv


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
        if isinstance(quantity, str):
            if not isinstance(float(quantity), float):
                if not isinstance(int(quantity), int):
                    raise ValueError('Количество должно быть целым числом')
        elif int(quantity) != float(quantity):
            raise ValueError('Количество должно быть целым числом')
        elif int(quantity) < 0:
            raise ValueError('Число должно быть неотрицательным')
        self.__name = name
        self.price = int(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты класса Item и дочерние от них")
        return self.quantity + other.quantity


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


    @classmethod
    def instantiate_from_csv(cls, file):
        cls.all.clear()
        with open(file, 'r', encoding='windows-1251') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=',')
            for row in csvreader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                item = cls(name, price, quantity)


    @staticmethod
    def string_to_number(str):
        return int(float(str))
