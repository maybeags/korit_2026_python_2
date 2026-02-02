from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ').lower()

    if choice == "off":
        is_on = False
        print('자판기가 종료되었습니다. 🙏')
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:
            continue

        if coffee_maker.is_resource_sufficient(drink= drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

# oop_version_kor 패키지 생성 -> menu / coffee_maker / money_machine / main 생성해서 그대로 다 붙여넣습니다.