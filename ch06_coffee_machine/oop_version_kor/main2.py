from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ').lower()

    if choice == "종료":             # 종료             동전 단위 고치겠습니다 : 쿼터 / 다임 / 니켈 / 페니
        is_on = False
        print('자판기가 종료되었습니다. 🙏')
    elif choice == "정산":     # 정산               재료 영어로 되어있는거 다 고칠겁니다 / 음료명도 고칠겁니다
        coffee_maker.report()                           # 드립 커피 20 소모 / 물 70 / 커피 2
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:
            continue

        if coffee_maker.is_resource_sufficient(drink= drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)