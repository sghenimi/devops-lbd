from abc import ABC, abstractmethod
from typing import List

# Single Responsibility Principle
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product):
        self.items.append(product)

    def get_total(self) -> float:
        return sum(item.price for item in self.items)

# Interface Segregation Principle
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> None:
        pass

# Open/Closed Principle & Liskov Substitution Principle
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Credit Card")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal")
        return True

class EmailNotifier(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotifier(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"SMS: {message}")

class DatabaseOrderRepository(OrderRepository):
    def save_order(self, order: Order) -> None:
        print(f"Saving order with {len(order.items)} items to database")

# Dependency Inversion Principle
class OrderService:
    def __init__(
        self,
        payment_processor: PaymentProcessor,
        notifier: NotificationSender,
        order_repository: OrderRepository
    ):
        self.payment_processor = payment_processor
        self.notifier = notifier
        self.order_repository = order_repository

    def process_order(self, order: Order) -> bool:
        total = order.get_total()

        if self.payment_processor.process_payment(total):
            self.order_repository.save_order(order)
            self.notifier.send_notification(f"Order processed successfully! Total: ${total}")
            return True
        else:
            self.notifier.send_notification("Payment failed!")
            return False

# Usage
def main():
    # Create products
    laptop = Product("Laptop", 999.99)
    mouse = Product("Mouse", 25.99)

    # Create order
    order = Order()
    order.add_item(laptop)
    order.add_item(mouse)

    # Configure services (Dependency Injection)
    payment_processor = CreditCardProcessor()
    notifier = EmailNotifier()
    order_repository = DatabaseOrderRepository()

    # Process order
    order_service = OrderService(payment_processor, notifier, order_repository)
    success = order_service.process_order(order)

    print(f"Order processed: {success}")

if __name__ == "__main__":
    main()