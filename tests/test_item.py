import pytest
from src.item import Item


@pytest.fixture
def item1 ():
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
        Item("Смартфон", -10000, 20)

def test_item_quantity():
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, '5')
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, 5.5)
    with pytest.raises(ValueError):
        Item("Ноутбук", 20000, -5)

def test_item_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_item_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    assert item2.price == 20000
