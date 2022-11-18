# from info import resources
import info

print("Hello and welcome in the coffee machine program")
print(info.resources)
print(info.MENU)


# Coffee Machine Program Requirements1.Prompt user by asking
# “​What would you like? (espresso/latte/cappuccino):
# ​”a.Check the user’s input to decide what to do next.
# b.The prompt should show every time action has completed,
# e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

def ask_user():
    #clear()
    user_choice = input("What would you like ? Espresso -> Type 1 , Latte -> Type 2, Cappuccino -> Type 3 :  ")
    if user_choice == "1":
        print("Go for a Espresso")
    elif user_choice == "2":
        print("Go for an Latte")
    elif user_choice == "3":
        print("Go for a Cappuccino")
    else:
        print("Bad choice choose something else")
    return user_choice

def check_enough_resources(choice):
    unable = False

    print("---------List ingredients to check-----------")
    print(info.MENU[choice]["ingredients"])
    print("Ressources available")
    print(info.resources)
    print("---------Fin Liste ingredients-----------")
    #print(info.MENU[choice]["ingredients"][ingredient_to_check])
    for ingredient in info.MENU[choice]["ingredients"]:
        #print(ingredient)
        if info.MENU[choice]["ingredients"][ingredient] > info.resources[ingredient]:
            unable = True
            print("")
            print("We have not enough")
            print(ingredient)
    if unable == True:
        print("Sorry we cannot deliver your drink")
    else:
        print("we can deliver your drink, please insert coins to get your drink")
    #for ingredient in info.MENU[choice]["ingredients"][ingredient_to_check]:
    #    print(ingredient)


    #print(type(info.MENU[choice][ingredient_to_check])
user_decision = ""
while (user_decision !="off"):
    user_decision = ask_user()
    if user_decision == "1":
        print("Lets see if we have a Espresso in stock")
        check_enough_resources("espresso")
    elif user_decision == "2":
        print("Lets see if we have an Latte in stock")
        check_enough_resources("latte")
    elif user_decision == "3":
        print("Lets see if we have a Cappuccino in stock")
        check_enough_resources("cappuccino")

#

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
