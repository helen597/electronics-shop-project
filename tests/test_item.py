import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all[0] == item1


def test_item_init(item2):
    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5
    assert Item.all[0] == item2


def test_item_init(item1, item2):
    assert Item.all[0] == item1
    assert Item.all[1] == item2


def test_item_price():
    with pytest.raises(ValueError):
        Item("Смартфон", 'abc', 20)
    with pytest.raises(ValueError):
        Item("Смартфон", - 10000, 20)
    with pytest.raises(ValueError):
        Item("Смартфон", '-10000', 20)


def test_item_quantity():
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, 'abc')
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, 5.5)
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, - 5)


def test_item_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_item_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    assert item2.price == 20000


def test_item_name_getter(item1, item2):
    assert item1.name == "Смартфон"
    assert item2.name == "Ноутбук"


def test_item_name_setter(item1, item2):
    item1.name = "СуперСмартфон"
    item2.name = "Ноут"
    assert item1.name == "СуперСмарт"
    assert item2.name == "Ноут"


def test_item_instantiate_from_csv():
    Item.all.clear()
    assert len(Item.all) == 0
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr(item1, item2):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_item_str(item1, item2):
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'
