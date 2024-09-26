#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        # Calculate the total price for the current item
        item_total = price * quantity
        # Add the total price to the register's total
        self.total += item_total
        # Add the items to the list of items
        self.items.extend([title] * quantity)
        # Keep track of the last transaction amount
        self.last_transaction_amount = item_total

    def apply_discount(self):
        if self.discount > 0:
            # Calculate the discount as a percentage off the total
            discount_amount = (self.discount / 100) * self.total
            # Apply the discount to the total
            self.total -= discount_amount
            # Return the updated total, converting it to an integer
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction amount from the total
        self.total -= self.last_transaction_amount


