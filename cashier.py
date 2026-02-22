class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        total = 0
        total += int(input("How many dollars?: ")) * 1.0
        total += int(input("How many half dollars: ")) * 0.5
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many nickles?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"Here is {change} in change")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False