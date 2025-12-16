# Coffee Machine - Fully Working Version

machine_default_stock = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}

type_of_coffee = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 20
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 100
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 70
    }
}

def check_for_resources_and_update(drink_type):
    """Check if enough resources and update stock if yes"""
    required = type_of_coffee[drink_type]
    
    if machine_default_stock["water"] < required["water"]:
        print("Sorry, not enough water.")
        return False
    if machine_default_stock["coffee"] < required["coffee"]:
        print("Sorry, not enough coffee.")
        return False
    if machine_default_stock["milk"] < required["milk"]:
        print("Sorry, not enough milk.")
        return False

    # Deduct resources
    machine_default_stock["water"] -= required["water"]
    machine_default_stock["coffee"] -= required["coffee"]
    machine_default_stock["milk"] -= required["milk"]
    
    return True

def process_coins():
    """Ask user for coins and return total amount paid"""
    print("Please insert coins (accepted: 1, 2, 5, 10, 20)")
    try:
        num_coins = int(input("How many coins are you inserting? "))
    except ValueError:
        print("Invalid input. Treating as 0 coins.")
        return 0

    total = 0
    for i in range(num_coins):
        try:
            coin = int(input(f"Coin {i+1}: "))
            if coin in [1, 2, 5, 10, 20]:
                total += coin
            else:
                print("Invalid coin! Not accepted.")
        except ValueError:
            print("Invalid input, skipping this coin.")

    print(f"Total amount inserted: {total}₹")
    return total

def print_report():
    """Show current resource levels"""
    print("\nCurrent Resource Levels:")
    print(f"Water: {machine_default_stock['water']}ml")
    print(f"Milk: {machine_default_stock['milk']}ml")
    print(f"Coffee: {machine_default_stock['coffee']}g")
    print(f"Money: {machine_default_stock['money']}₹\n")

# Main Program
machine_on = True
print("Welcome to the Coffee Machine!")

while machine_on:
    print("\n" + "="*40)
    print("          COFFEE MENU")
    print("="*40)
    print("espresso  - 20₹")
    print("latte     - 100₹")
    print("cappuccino - 70₹")
    print("Type 'report' to see stock")
    print("Type 'off' to turn off the machine")
    print("-"*40)

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    # Turn off the machine
    if choice == "off":
        print("Turning off the machine... Goodbye!")
        machine_on = False
        continue

    # Show report
    elif choice == "report":
        print_report()
        continue

    # Check if valid drink
    if choice not in type_of_coffee:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
        continue

    drink = choice
    price = type_of_coffee[drink]["price"]

    print(f"\nYou selected: {drink.capitalize()}")
    print(f"That will be {price}₹. Please insert coins.")

    # Process payment (only once!)
    amount_paid = process_coins()

    if amount_paid < price:
        print("Sorry, that's not enough money. Amount refunded.")
    else:
        # Check resources
        if check_for_resources_and_update(drink):
            machine_default_stock["money"] += price
            change = amount_paid - price
            if change > 0:
                print(f"Here is your change: {change}₹")
            print(f"Here is your {drink} ☕ Enjoy your coffee!")
        else:
            print("Sorry, not enough ingredients. Your money has been refunded.")
