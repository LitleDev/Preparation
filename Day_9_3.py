#Liskov Substitution Principle
# Subcl;ass should be replaceable without breaking functionality

class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Charging {amount} to credit card")

class CashProcessor(PaymentProcessor):
    def process_payment(self, amount):
        raise Exception("Cash cannot be processed digitally!")

# all subclasses can be safely substituted.

class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Charging {amount} to credit card")

class CashProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Accepting {amount} in cash")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Transferring {amount} via PayPal")


def checkout(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

checkout(CreditCardProcessor(), 100)
checkout(CashProcessor(), 50)
checkout(PayPalProcessor(), 200)
