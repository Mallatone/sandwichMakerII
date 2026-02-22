import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("\nWhat would you like? (small/medium/large/off/report): ").lower()

        match choice:
            case "off":
                is_on = False
                print("System shutting down.")

            case "report":
                for item, amount in sandwich_maker_instance.machine_resources.items():
                    print(f"{item.capitalize()}: {amount}")

            case "small" | "medium" | "large":
                sandwich = recipes[choice]
                if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                    payment = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(payment, sandwich["cost"]):
                        sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

            case _:
                print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()