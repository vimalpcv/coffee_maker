from data import *


def report():
    print(report_text, "--Ingredients--", sep='\n')
    for key, value in RESOURCES.items():
        if key == 'money':
            print("--Money--")
            total_amount = 0
            for key_m, value_m in RESOURCES[key].items():
                print(f"{key_m.capitalize()} : ${value_m}")
                total_amount += value_m * VALUES[key_m]
            print(f"Total money available is ${round(total_amount, 2)}")
        else:
            print(f"{key.capitalize()} : ${value}")
    print("-------------------------------")


def show_menu():
    print(menu_text)
    for key_name, value in MENU.items():
        print(f"{key_name.capitalize()} is price for ${value['cost']}")


def is_resource_sufficient(ordered_item):
    is_enough = True
    for ingredient_key, ingredient_value in ordered_item['ingredients'].items():
        if RESOURCES[ingredient_key] < ingredient_value:
            print(f" Sorry there is not enough {ingredient_key.capitalize()}.")
            is_enough = False
    return is_enough


def make_coffee(ordered_item):
    for ingredient_name, ingredient_value in ordered_item['ingredients'].items():
        RESOURCES[ingredient_name] -= ingredient_value


def refund_money(refund):
    refund_dummy = refund
    for coin_name in MONEY:
        if refund == 0:
            break
        while MONEY[coin_name] > 0 and refund >= VALUES[coin_name]:
            refund -= VALUES[coin_name]
            MONEY[coin_name] -= 1
    print(f"Here is ${round(refund_dummy, 2)} dollars in change.")


def load_money(ordered_name, ordered_cost):
    loaded = True
    loaded_money = {}
    loaded_money_value = 0
    for coin_name, coin_value in VALUES.items():
        loaded_money[coin_name] = int(
            input(f"how many {coin_name.capitalize()}: ") or '0')
        loaded_money_value += loaded_money[coin_name] * coin_value
    loaded_money_value = round(loaded_money_value, 2)
    print(f"Total money loaded is ${loaded_money_value}")

    if loaded_money_value < ordered_cost:
        loaded = False
        print(
            f"Sorry that's not enough money. Money refunded. The cost of {ordered_name} is ${ordered_cost}")
    else:
        for key, value in loaded_money.items():
            MONEY[key] += value

        # Initiate refund
        if loaded_money_value > ordered_cost:
            difference = round(loaded_money_value - ordered_cost, 2)
            refund_money(difference)

    return loaded


def coffee_machine():
    is_on = True
    while is_on:
        requirement = input(
            "What would you like? (espresso/latte/cappuccino): ")

        if requirement == 'off':
            is_on = False
        elif requirement == "report":
            report()
        elif requirement == 'menu':
            show_menu()
        elif requirement in MENU:
            ordered_item = MENU[requirement]
            availability = is_resource_sufficient(ordered_item)
            if availability:
                if load_money(ordered_name=requirement, ordered_cost=ordered_item['cost']):
                    make_coffee(ordered_item)
                    print(coffee_ready)
        else:
            print('Invalid input')


print(title_text)
coffee_machine()
print(bye_text)
