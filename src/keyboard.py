from src.item import Item


class Mixin:
    """Класс-миксин"""

    def __init__(self, name, price, quantity, language):
        """Инициализация

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Раскладка клавиатуры.
        """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language
    #
    # @language.setter
    # def language(self, language):
    #     self.__language = language

    def change_lang(self):
        """
        Меняет раскладку клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Mixin, Item):
    """Класс для товара 'Клавиатура'"""

    def __init__(self, name, price, quantity, language="EN"):
        """Создание экземпляра класса клавиатура"""
        super().__init__(name, price, quantity, language)
