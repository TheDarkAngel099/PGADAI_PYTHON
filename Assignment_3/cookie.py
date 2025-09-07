from dessert_item import DessertItem

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def get_cost(self):
        return (self.quantity / 12) * self.price_per_dozen
