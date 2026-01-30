from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# cappuccino의 우유 소모량을 print() 하시오.
print(menu.menu[2].ingredients['milk'])

# coffee_maker에서의 커피 양 - 에스프레소의 커피 양을 한 결과값을
#print() 하시오.

print(coffee_maker.resources['coffee'] - menu.menu[1].ingredients['coffee'])

# main 단계 작성 시작
is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ').lower()   # get_items의 return값이 어떻게 되는지 확인하면 좋겠습니다.
    # todo - 1 : choice 가 off / report / 오타났을 때 작성하는 부분을 작성하시오. 각 클래스의 .report() 메서드를 꼭꼭꼭꼭 확인하시오.
    if choice == "off":
        is_on = False
        print('자판기가 종료되었습니다. 🙏')
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print('잘못입력하셨습니다.')     # 현재는 off / report 아니면 다 잘못되겠네요.