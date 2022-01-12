from dataclasses import dataclass, field
from enum import Enum, auto

class OrderStatus(Enum):
    OPEN = auto()
    PAID = auto()
    CANCELLED = auto()
    DELIVERED = auto()
    RETURNED = auto()
    IN_TRANSIT = auto()


@dataclass
class Order:
    customer_id: str = ""
    customer_name: str = ""
    customer_address: str = ""
    customer_zip_code: str = ""
    customer_city: str = ""
    customer_country: str = ""
    customer_phone_number: str = ""
    customer_email_address: str = ""
    items: list[str] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    quantity: list[int] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id : str = ""

    def create_line_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.prices.append(price)
        self.quantity.append(quantity)
    
    def set_status(self, status: OrderStatus):
        self._status = status