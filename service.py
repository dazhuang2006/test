from models import Order
from pricing import total


def checkout(order: Order) -> dict:
    return {
        "amount": round(total(order), 2),
        "count": sum(p.qty for p in order.items),
    }
