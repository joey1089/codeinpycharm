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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Print report of the coffee machine resources
def format_data(item):
    """ Format account into printable format: item-water,item-milk and item-coffee. without money. """
    item_water = item["water"]
    item_milk = item["milk"]
    item_coffee = item["coffee"]
    return f"Currently available resources:\n Water: {item_water}ml \n Milk: {item_milk}ml \n Coffee: {item_coffee}g"


maintainers = input("Type 'off' to switch of the machine for maintenance or 'no' to continue : ").lower()
count = 0
while maintainers != "off":
    count += 1
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "espresso":
        print("It's $2.50")
    elif user_choice == "latte":
        print("It's $1.50")
    else:
        print("It's $3.00")
    if count > 1:
        break
    print()

# TODO: 2. Check the resources are sufficient?

 get_report = format_data(resources)     # check if the resources are sufficient for making anymore coffees


# TODO: 3. Process Coins
# TODO: 4. Check transaction is successful?
# TODO: 5. Make Coffee
