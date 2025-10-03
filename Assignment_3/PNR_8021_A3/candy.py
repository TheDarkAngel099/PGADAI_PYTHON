from dessert_item import DessertItem

class Candy(DessertItem):
    def __init__(self, name , weight_gms, price_per_kg):
        super().__init__(name)
        self.weight_gms = weight_gms
        self.price_per_kg = price_per_kg

    def get_cost(self):
        return (self.weight_gms/1000) * self.price_per_kg