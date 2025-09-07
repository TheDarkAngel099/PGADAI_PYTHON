from dessert_item import DessertItem

class IceCream(DessertItem):
    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost

    def get_cost(self):
        return self.cost

class Sundae(IceCream):
    def __init__(self, name, cost, topping_name, topping_cost):
        super().__init__(name, cost)
        self.topping_name = topping_name
        self.topping_cost = topping_cost

    def get_cost(self):
        return self.cost + self.topping_cost
