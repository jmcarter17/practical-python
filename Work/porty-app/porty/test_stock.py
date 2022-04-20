import pytest

from porty import stock


def test_createstock():
    s = stock.Stock("GOOG", 100, 490.1)
    assert s.name == "GOOG"
    assert s.shares == 100
    assert s.price == 490.1
    assert s.cost == 49010.0


def test_sellstock():
    s = stock.Stock("GOOG", 100, 450.0)
    s.sell(25)
    assert s.shares == 75
    assert s.cost == 450 * 75


def test_bad_input():
    s = stock.Stock("GOOG", 100, 450.0)
    with pytest.raises(TypeError):
        s.shares = '200'
    with pytest.raises(TypeError):
        s.name = 1234
    with pytest.raises(TypeError):
        s.price = 123
