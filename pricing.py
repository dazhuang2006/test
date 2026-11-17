from models import Order

VIP_DISCOUNT = 0.15
TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 100


def subtotal(order: Order) -> float:
    return sum(p.price * p.qty for p in order.items)


def discount(order: Order) -> float:
    """VIP 订单满 100 打 85 折。"""
    if order.vip and subtotal(order) >= DISCOUNT_THRESHOLD:
        return subtotal(order) * VIP_DISCOUNT
    return 0.0


def total(order: Order) -> float:
    base = subtotal(order) - discount(order)
    return base + base * TAX_RATE
