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
        drink = menu.find_drink(choice)
        if drink == None:
            continue # 이하의 코드는 실행되지 않고 아예 다음 반복으로 넘기는 키워드

        if coffee_maker.is_resource_sufficient(drink= drink):     # argument로 객체가 들어가야합니다. 왜 ? 로직보니까 drink에 ingredients라는 속성이 있는 것을 확인했기 때문에.
            # 고려 사항 # 1 -> money_machine의 make_payment() 메서드 내에 process_coins()가 호출되고 있다는 점 -> 지불 하기 전에 돈 계산하는 process_coins() 메서드를 따로 호출할 필요가 없다.
            # 고려 사항 # 2 -> make_payment()의 return 타입이 True / False 형이다 -> 어디에 자주 쓴다? -> 조건문에 자주 쓴다.
            if money_machine.make_payment(drink.cost):    # cost라는 매개변수가 존재하네요. 뭔지 확인하기 위해서 로직을 봐야 합니다.
                # 내부 로직을 확인했을 때 음료 가격만큼 뺐다는 것을 알 수 있습니다. drink는 음료 객체를 나타내는데, drink에서 cost값을 불러오기 위한 코드가 뭔지 알아봐야겠네요.
                coffee_maker.make_coffee(drink)




        # 음료 이름을 입력 받은 시점부터의 프로세스를 떠올려서 코드를 작성하셔야만 합니다. 이때 고려해야할 것은 절차지향 방식으로 코딩했을 때의 과정과, 현재 참조해야 하는 파이썬 모듈들의 매개변수 차이와 메서드 작동 원리의 차이를 감안해서 코드를 쓸 필요가 있다는 점입니다.
        # pop version의 함수 작성 순서대로 저희가 작동하도록 했습니다.
        # is_resources_enough(order_ingredient) / is_resource_sufficient(drink)
        # 재료가 충분한지 여부의 return 타입 확인해보시면 True / False입니다. 얘가 통과해야지 돈내는 내용이 될건데 make_payment()가 또 True/False입니다. 이거 통과하면 커피가 나와야 하네요.