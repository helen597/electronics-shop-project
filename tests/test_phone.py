import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("Philips", 10000, 20, 1)

@pytest.fixture
def phone2():
    return Phone("Motorola", 20000, 5, 2)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_phone_init(phone1):
    assert Phone.all == []
    assert phone1.name == "Philips"
    assert phone1.price == 10000
    assert phone1.quantity == 20
    assert Phone.all[0] == phone1


def test_phone_init(phone2):
    assert phone2.name == "Motorola"
    assert phone2.price == 20000
    assert phone2.quantity == 5
    assert Phone.all[0] == phone2


def test_phone_init(phone1, phone2):
    assert Phone.all[0] == phone1
    assert Phone.all[1] == phone2


def test_phone_add(phone1, phone2, item1, item2):
    assert item1 + item2 == 25
    assert phone1 + phone2 == 25
    assert phone1 + item1 == 40
    with pytest.raises(ValueError):
        assert phone1 + 123 == 143


def test_phone_repr(phone1, phone2):
    assert repr(phone1) == "Phone('Philips', 10000, 20, 1)"
    assert repr(phone2) == "Phone('Motorola', 20000, 5, 2)"


def test_phone_str(phone1, phone2):
    assert str(phone1) == 'Philips'
    assert str(phone2) == 'Motorola'


def test_phone_number_of_sim_getter(phone1, phone2):
    assert phone1.number_of_sim == 1
    assert phone2.number_of_sim == 2


def test_phone_number_of_sim_setter(phone1):
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
