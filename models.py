from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    qty: int = 1


@dataclass
class Order:
    items: list[Product] = field(default_factory=list)
    vip: bool = False
