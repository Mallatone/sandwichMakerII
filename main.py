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
        # Users choice
        choice = input("\nWhat would you like? (small/medium/large/off/report): ").lower()

        match choice:
            case "off": # Shuts down program
                is_on = False
                print("System shutting down.")

            case "report": # Report total amount of resources
                for item, amount in sandwich_maker_instance.machine_resources.items():
                    print(f"{item}: {amount}")

            case "small" | "medium" | "large":
                sandwich = recipes[choice]
                if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                    payment = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(payment, sandwich["cost"]):
                        sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

            case _: # Loops until correct choice is made
                print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()