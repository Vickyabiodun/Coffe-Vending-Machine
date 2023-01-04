MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# profit stores the total amount of money that the vending machine has made from coffee sales
profit = 0

# resources stores the current amount of ingredients that the vending machine has
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    # check if the vending machine has enough ingredients to make the chosen coffee
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    # check if the payment received is sufficient to cover the cost of the chosen coffee
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # update the global profit variable
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    # deduct the ingredients used from the resources dictionary
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# set is_on to True to run the vending machine loop
is_on = True

# run the vending machine loop until the user enters "off"
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        # set is_on to False to exit the loop
        is_on = False
    elif choice == "report":
        # print the current amount of each ingredient and the total profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # get the chosen coffee from the MENU dictionary
        drink = MENU[choice]
        # check if there are sufficient ingredients to make the chosen coffee
        if is_resource_sufficient(drink["ingredients"]):
            # accept payment
            payment = process_coins()
            # check if the payment is sufficient
            if is_transaction_successful(payment, drink["cost"]):
                # dispense the chosen coffee
                make_coffee(choice, drink["ingredients"])

