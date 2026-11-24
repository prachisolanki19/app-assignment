# Strategy Pattern: Configurable Payment Processing System

# Step 1: Create a base Strategy class
class PaymentStrategy:
    def pay(self, amount):
        pass


# Step 2: Implement different payment strategies

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Bitcoin.")


# Step 3: Create the Payment Context class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Step 4: Main program
print("===== PAYMENT PROCESSING SYSTEM =====")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Select your payment method: "))
amount = float(input("Enter payment amount: Rs. "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
elif choice == 3:
    strategy = BitcoinPayment()
else:
    print("Invalid payment method!")
    exit()

# Create processor and process payment
processor = PaymentProcessor(strategy)
processor.process_payment(amount)