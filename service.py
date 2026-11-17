from models import Order
from pricing import total


def checkout(order: Order) -> dict:
    return {
        "amount": round(total(order), 2),
        "count": sum(item.qty for item in order.items),
    }
