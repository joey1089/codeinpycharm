from random import choice
import re
from traceback import print_tb

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import os


def clrscr():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_report(resource, money):
    """ Reports all resources available for making different coffee flavours. """
    item_water = resource['water']
    item_milk = resource['milk']
    item_coffee = resource['coffee']
    money = profit
    return f"\n Water : {item_water} ml  \n Milk : {item_milk} ml \n Coffee: {item_coffee} g\n Money :$ {money}\n"

def is_sufficient(drink_name,use_ingredients):
    for item in use_ingredients:
        if use_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        print("Insert required coins")
        return True

def process_coins():
    total = int(input("How many quarters : ")) * 0.25
    total += int(input("how many dims : ")) * 0.10
    total += int(input("how many nickles : ")) * 0.05
    total += int(input("how many pennies : ")) * 0.01
    return round(total,2)


#TODO : 1.Check if the machine is on and will want to switch it off for maintenance
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(get_report(resources,profit))
    else:
        drink = MENU[choice]
        if is_sufficient(resources,drink['ingredients']):
            payment = process_coins()
            print(f"money received ${payment}")
