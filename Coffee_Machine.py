from menu_coffee_machine import MENU
from menu_coffee_machine import resources
from menu_coffee_machine import coins


def resources_checking(choice):
    """checking if there are enough resources in the machine to make  a chosen coffee"""
    for i in MENU[choice]["ingredients"]:
        # print(i)
        # print(MENU[choice]["ingredients"][i])
        if MENU[choice]["ingredients"][i] > resources[i]:
            print(f"Sorry, there is no enough {i}")
            return
    return "ok"


def money_checking():
    """to calculate the coins that customers put in"""
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    sum = coins["quarters"] * quarters + coins["dimes"] * dimes + coins["nickles"] * nickles + coins["pennies"] * pennies
    return sum


def enough_money(original_cost, money_putin):
    """checking if customers have put in enough money, if so, make the coffee, otherwise return the money to customers"""
    if original_cost > money_putin:
        print("Sorry, that's not enough money. Money Refunded")
        return "sorry"
    return print(f"Here is ${original_cost - money_putin} in change. \nHere is your {coffee_choice} ☕. Enjoy!")


while True:
    coffee_choice = input("What would you like?(espresso/latte/cappuccino): \n")
    if coffee_choice == "":
        break
    result = resources_checking(coffee_choice)
    print("Please insert coins.")
    money_putin = money_checking()
    make_coffee = enough_money(MENU[coffee_choice]["cost"], money_putin)

    if result == "ok" and make_coffee != "sorry":
        # check the current resources again after deduction
        for a in MENU[coffee_choice]["ingredients"]:
            resources[a] = resources[a] - MENU[coffee_choice]["ingredients"][a]
            print(resources[a])
            print(f"Profit: {MENU[coffee_choice]['cost']}")


