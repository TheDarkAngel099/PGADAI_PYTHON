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

        print(checkout.get_invoice())

        checkout.clear()
        (checkout.get_total_cost())  # Will raise exception

    except CartIsEmptyException as ce:
        print("Error:", ce)
    except AmountInvalidException as ae:
        print("Error:", ae)

if __name__ == "__main__":
    run_checkout()
