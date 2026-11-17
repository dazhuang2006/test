import pytest

from models import Order, Product
from pricing import discount, subtotal, total
from service import checkout


def order(*items, vip=False):
    return Order(items=list(items), vip=vip)


def test_subtotal():
    o = order(Product("A", 50, 2), Product("B", 10, 1))
    assert subtotal(o) == 110


def test_vip_discount_at_threshold():
    o = order(Product("A", 100, 1), vip=True)
    assert discount(o) == pytest.approx(15)


def test_vip_discount_below():
    o = order(Product("A", 99, 1), vip=True)
    assert discount(o) == 0


def test_total_with_tax():
    o = order(Product("A", 100, 1), vip=True)
    assert total(o) == pytest.approx(91.8)


def test_checkout_count():
    o = order(Product("A", 50, 2), Product("B", 10, 1))
    assert checkout(o)["count"] == 3
