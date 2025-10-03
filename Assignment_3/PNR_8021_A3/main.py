from candy import Candy
from cookie import Cookie
from ice_cream import IceCream, Sundae
from checkout import Checkout
from exceptions import CartIsEmptyException, AmountInvalidException

def run_checkout():
    checkout = Checkout()
    try:
        checkout.enter_item(Candy("Fudge", 200, 50))
        checkout.enter_item(Cookie("ChocoChip", 4, 10))
        checkout.enter_item(IceCream("Vanilla", 25))
        checkout.enter_item(Sundae("Strawberry", 30, "Sprinkles", 10))
        checkout.enter_item(Candy("Mango Bite", 150, 30))
        checkout.enter_item(Candy("Eclairs", 300, 40))
        checkout.enter_item(Candy("Pulse", 250, 35))
        checkout.enter_item(Cookie("Oreo Crunch", 5, 12))
        checkout.enter_item(Cookie("Butter Delight", 6, 8))
        checkout.enter_item(Cookie("Nutty Buddy", 7, 15))
        checkout.enter_item(IceCream("Chocolate", 35))
        checkout.enter_item(IceCream("Butterscotch", 30))
        checkout.enter_item(IceCream("Mint Chip", 28))
        checkout.enter_item(Sundae("Choco Storm", 40, "Choco Chips", 15))
        checkout.enter_item(Sundae("Berry Blast", 45, "Blueberry Sauce", 20))
        checkout.enter_item(Sundae("Tropical Twist", 50, "Pineapple", 18))
        print(checkout.get_invoice())

        # Clear cart and trigger exception
        checkout.clear()
        checkout.get_total_cost()  # Will raise exception

    except CartIsEmptyException as ce:
        print("Error:", ce)
    except AmountInvalidException as ae:
        print("Error:", ae)

if __name__ == "__main__":
    run_checkout()