from menu_coffee_machine import MENU
from menu_coffee_machine import resources
from menu_coffee_machine import coins

print(MENU["espresso"]["ingredients"]["water"])

coffee_choice = input("What would you like?(espresso/latte/cappuccino): \n")

# resources_checking
def resources_checking(choice):
    for i in MENU[choice]["ingredients"]:
        print(i)
        print(MENU[choice]["ingredients"][i])
        if MENU[choice]["ingredients"][i] > resources[i]:
            print(f"Sorry, there is no enough {i}")
            return

resources_checking(coffee_choice)
print("Please insert coins.")


def money_checking():
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    sum = coins["quarters"] * quarters + coins["dimes"] * dimes + coins["nickles"] * nickles + coins["pennies"] * pennies
    return sum

# compare the coins inserted with the cost
def enough_money(original_cost, money_putin):
    if original_cost > money_putin:
        print("Sorry, that's not enough money. Money Refunded")
        return
    else:
        print(f"Here is ${original_cost - money_putin} in change.")
        print("Here is your {coffee_choice} ☕. Enjoy!")

# check the current resources again after deduction


