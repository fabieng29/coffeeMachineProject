# from info import resources
import info
from os import system, name


def clear():
    """Define the clear function"""
    # for windows
    print(name)
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Coffee Machine Program Requirements1.Prompt user by asking
# “​What would you like? (espresso/latte/cappuccino):
# ​”a.Check the user’s input to decide what to do next.
# b.The prompt should show every time action has completed,
# e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
def is_transaction_success(money_introduced, cost_drink,drink_chosen):
    """Check if transaction is successful, deliver drink and give money back"""
    money_back = round(money_introduced - cost_drink,2)
    global profit
    if money_introduced>=cost_drink:
        print("Transaction successful")
        print(f"You have inserted $ {money_introduced} and the cost of the drink was $ {cost_drink}")
        print(f"Enjoy your {drink_chosen}")
        deliver_drink(drink_chosen)
        profit += cost_drink
        print(f"Here is your money back $ {money_back} ")
        return True
    else:
        print(f"Sorry there is not enough money, here is your $ {money_introduced} back")
    return False

def insert_money():
    """Count how many money the customer has inserted"""
    total = int(input("How many quarters: "))*0.25
    total += int(input("How many dimes: "))*0.1
    total += int(input("How many nicket: "))*0.05
    total +=  int(input("How many pennies: "))*0.01
    return total

def deliver_drink(drink_chosen):
    """Substract the amount of ingredients required to deliver the drink to the resources"""
    for ingredient in info.MENU[drink_chosen]["ingredients"]:
        info.resources[ingredient] = info.resources[ingredient] - info.MENU[drink_chosen]["ingredients"][ingredient]

def ask_user():
    """Ask the user to choose a drink, allow the user to check the resources available. An option is available
    to enter in maintenance mode """
    # clear()
    user_choice = input("What would you like ? Espresso -> Type 1 , Latte -> Type 2, Cappuccino -> Type 3 :  ")
    if user_choice == "1":
        if check_enough_resources("espresso"):
            money_given = insert_money()
            is_transaction_success(money_given, info.MENU["espresso"]["cost"], "espresso")
    elif user_choice == "2":
        if check_enough_resources("latte"):
            money_given = insert_money()
            is_transaction_success(money_given, info.MENU["latte"]["cost"], "latte")
    elif user_choice == "3":
        if check_enough_resources("cappuccino"):
            money_given = insert_money()
            is_transaction_success(money_given, info.MENU["cappuccino"]["cost"], "cappuccino")
    elif user_choice == "off":
        print("Maintenance mode")
    elif user_choice == "report":
        print("Here are the resources available")
        unit = ""
        for ingredient in info.resources:
            if ingredient == "coffee":
                unit = "g"
            else:
                unit = "ml"
            print(f"We have {info.resources[ingredient]} {unit} {ingredient} available in stock")
        print(f"Money = {profit}")
    else:
        print("Bad choice choose something else")
    return user_choice


def check_enough_resources(choice):
    """Check if there is enough ingredients to deliver the drink"""
    able_to_deliver = True
    for ingredient in info.MENU[choice]["ingredients"]:
        if info.MENU[choice]["ingredients"][ingredient] > info.resources[ingredient]:
            able_to_deliver = False
            print(f"We have not enough {ingredient}")
    if not able_to_deliver:
        print("Sorry we cannot deliver your drink")
    else:
        print("we can deliver your drink, please insert coins to get your drink")
        print("We accept quarters $0.25, dimes $0.10, nickles $0.05 and pennies $0.01")
    return able_to_deliver


profit = 0
print("Hello and welcome in the coffee machine program")
user_decision = ""
while user_decision != "off":
    user_decision = ask_user()
    clear()





# 2.Turn off the Coffee Machine by entering “​off​” to the prompt.
# a.For maintainers of the coffee machine, they can use “off” as the secret word to turn offthe machine. Your code should end execution when this happens.
#
# 3.Print report.a.When the user enters “report” to the prompt, a report should be generated that showsthe current resource values.
# e.g.Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.54.Check resources sufficient?
# a.When the user chooses a drink, the program should check if there are enoughresources to make that drink.
# b.E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It shouldnot continue to make the drink but print:
# “​Sorry there is not enough water.​”c.The same should happen if another resource is depleted, e.g. milk or coffee.
#
# 5.Process coins.
# a.If there are sufficient resources to make the drink selected, then the program shouldprompt the user to insert coins.
# b.Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01c.Calculate the monetary value of the coins inserted.
# E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.526.Check transaction successful?
# a.Check that the user has inserted enough money to purchase the drink they selected.E.g Latte cost $2.50, but they only inserted $0.52
# then after counting the coins theprogram should say “​Sorry that's not enough money. Money refunded.​”.
# b.But if the user has inserted enough money, then the cost of the drink gets added to themachine as the profit and this will be reflected the next time “report” is triggered.
# E.g.Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.5c.If the user has inserted too much money, the machine should offer change
