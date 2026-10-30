# Ouvert à l’extension, fermé à la modification :
# Une classe doit pouvoir être étendue sans avoir à la modifier.

from abc import ABC, abstractmethod
from typing import Mapping

class Widget():
    def get_dashboard_widget_data(self, id: str) -> Mapping:
        ...

    def get_pdf_widget_data(self, id: str) -> Mapping:
        ...

# Definition: Software entities should be open for extension but closed for modification.
#Problems: Adding new widget methods requires modifying existing code.

class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing ${amount} via Credit Card")
        elif payment_type == "paypal":
            print(f"Processing ${amount} via PayPal")
        elif payment_type == "bitcoin":  # New requirement
            print(f"Processing ${amount} via Bitcoin")
        # Need to modify this method for each new payment type

#Good
class Widget(ABC):

    @abstractmethod
    def get_data(self, id: str) -> Mapping:
        ...

# Si on veut un widget différent, mieux vaut créer une hiérarchie :
# Ainsi, on étend le comportement sans toucher à la classe de base.
class WidgetDashBoard(Widget):
    def get_data(self, id: str) -> Mapping:
        ...

class PDFWidget(Widget):
    def get_data(self, id: str) -> Mapping:
        ...

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via PayPal")

class BitcoinPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Bitcoin")

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.process(amount)

# Usage
processor = PaymentProcessor()
processor.process_payment(CreditCardPayment(), 100)
processor.process_payment(PayPalPayment(), 50)
processor.process_payment(BitcoinPayment(), 75)