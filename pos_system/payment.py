from typing import Protocol

from pos_system.order import Order


class PaymentServiceConnectionError(Exception):
    """ Custom error raised when we cannot connect to the payment service. """

class OrderRepository(Protocol):

    def find_order(self, order_id: str) -> Order:
        ...
    
    def compute_order_total_price(self, order: Order) -> int:
        ...


class StripePaymentProcessor:
    def __init__(self, system: OrderRepository):
        self.connected = False
        self.system = system
    
    def connect_to_service(self, url: str) -> None:
        print(f"Connecting to payment processing service at url {url}... done!")
        self.connected = True
    
    def process_payment(self, order_id: str) -> None:
        if not self.connected:
            raise PaymentServiceConnectionError()
        order = self.system.find_order(order_id=order_id)
        total_price = self.system.compute_order_total_price(order)
        print(
            f"Processing payment of ${total_price}, reference {order.id}"
        )