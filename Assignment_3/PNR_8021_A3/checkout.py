from dessert_item import DessertItem
from exceptions import CartIsEmptyException, AmountInvalidException


class Checkout:
    def __init__(self):
        self.cash_register = []

    def enter_item(self, item):
        if not isinstance(item, DessertItem):
            raise AmountInvalidException("Only DessertItem objects can be added.")
        self.cash_register.append(item)

    def clear(self):
        self.cash_register.clear()

    def get_item_count(self):
        return len(self.cash_register)

    def get_total_cost(self):
        if not self.cash_register:
            raise CartIsEmptyException("Cart is empty. Cannot calculate total.")
        return sum(item.get_cost() for item in self.cash_register)

    def get_invoice(self):
        if not self.cash_register:
            raise CartIsEmptyException("Cart is empty. Cannot generate invoice.")
        invoice = "----- INVOICE -----\n"
        for item in self.cash_register:
            invoice += f"{item.get_name():20} ₹{item.get_cost():.2f}\n"
        invoice += f"\nTotal Cost: ₹{self.get_total_cost():.2f}"
        return invoice
