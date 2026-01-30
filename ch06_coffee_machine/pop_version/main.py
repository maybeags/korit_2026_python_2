MENU = {                    # 다 하신 분들은 카푸치노의 커피 소모량을 콘솔에 출력하시오.
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    },
    "라떼": {
        "재료" : {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
}

profit = 0

# 에스프레소의 가격만큼 profit을 증가시키고 print(profit)이라고 했을 때 1.5가 출력될 수 있도록 print()문을 작성하시오.
# profit += MENU["에스프레소"]["가격"]
# print(profit)
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}

# 라떼를 주문하면 생기는 물/커피/우유의 소모량만큼 resources에서 빼고, print(resources)를 했을 때 그 결과가 반영되도록 코드를 작성하시오.
# 또한 라떼를 주문했기 때문에 profit에 라떼 가격만큼 증가시켜 print(profit)을 통해 2.5달러를 출력하시오.

# resources["물"] -= MENU["라떼"]["재료"]["물"]
# resources["우유"] -= MENU["라떼"]["재료"]["우유"]
# resources["커피"] -= MENU["라떼"]["재료"]["커피"]
# print(resources)
# profit += MENU["라떼"]["가격"]
# print(profit)
# 근데 resources 마이너스 시키는 부분을 확인해보면 얘가 포켓몬 할 때처럼 index가 아닐 뿐이지 기본적으로 반복이 된다는 사실을 알 수 있습니다. -> key를 기준으로.

# print(resources)
# for stuff in resources:
#     # print(stuff, end=" / ")
#     resources[stuff] -= MENU["라떼"]["재료"][stuff] #라떼의재료의물/우유/커피를 의미하는 코드만 써주면
#
# print(resources)

# 함수 정의 영역
def is_resources_enough(order_ingredients):     # MENU[choice]["재료"]
    """"DocString : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True 반환, 아니면 False 반환
    :param: order_ingredients
    :return: True / False
     """""
    for item in order_ingredients:      #MENU[choice]["재료"]가 반복돌아갔으니까 물/우유/커피 가 나옵니다.
        if resources[item] < order_ingredients[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다. 🙏")
            return False
    return True     #위의 조건문이 실행이 안된다면 전체 재료가 충분히 있으므로 True 리턴

def process_coins():
    """동전 들을 입력 받아 전체 금액을 반환하는 함수 call3() 유형"""
    '''
    쿼터, 다임, 니켈, 페니 네 종류의 동전
    쿼터 = 0.25 달러
    다임 = 0.1 달러
    니켈 = 0.05 달러
    페니 = 0.01 달러   quarter, dime, nickel, penny 라는 스펠링을 가집니다.
    '''
    sum = 0
    # 여기다가 로직 작성하세요.
    # quarter = int(input('쿼터 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.25
    # dime = int(input('다임 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.1
    # nickel = int(input('니켈 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.05
    # penny = int(input('페니 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.01
    # sum = quarter + dime + nickel + penny
    sum += int(input('쿼터 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.25
    sum += int(input('다임 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.1
    sum += int(input('니켈 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.05
    sum += int(input('페니 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.01
    return sum

def is_transaction_successful(money_received, drink_cost) :    # 보통 is로 시작하면 bool 타입
    """process_coins()의 결과값과 음료 가격을 매개변수로 삼아 동전이 가격보다 높으면 True / 아니면 False 반환. 그리고 True라면 profit에 음료가격만큼 추가해주고, 잔돈 반환하는 출력문을 작성해야 합니다.
    :params: money_received, drink_cost
    :return: True / False"""
    # 내부 로직 작성하셔야 합니다.
    charge = money_received - drink_cost
    if charge >= 0:
        print(f'잔돈 ${charge}를 반환합니다.')
        global profit
        profit+= drink_cost    # 함수 내에서 전역 변수인 profit 값을 바꾸려고 하기 때문에 오류
        # 함수를 통해서 전역 변수의 값을 바꾸고자 할 때는 변수명 앞에 global이라고 명시해줘야 합니다.
        return True
    else:
        print(f'동전이 충분하지 않습니다. 금액 ${money_received}를 반환합니다.')
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료명"]["재료"]들을 차감함.
        -> 차감은 무조건 이루어지겠네요. 돈도 다 있고 재료도 충분했으니까.
    """
    # main 단계에서 작성한 것과 is_resources_enough 코드를 참조하여 로직을 작성하시오.
    for stuff in order_ingredients:
        resources[stuff] -= order_ingredients[stuff]
    print(f'{choice}☕가 나왔습니다. 맛있게 드세요 ! ❤️')

is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    # drink = MENU[choice]  여기에 선언하면 report/off/혹은 오타가 MENU의 키로 대입돼서 오류가 발생할 수 있습니다.
    # 만약에 choice가 "off"라면 자판기 종료 메시지를 출력하고 종료.
    if choice == "off":
        print("자판기가 종료되었습니다. ⭐")
        is_on = False
    # "report"라면 현재 자판기의 물 / 우유 / 커피의 양과 돈의 양을 보여줄 것
    elif choice == "report":
        print(f"물 : {resources["물"]} ml\n우유: {resources["우유"]} ml\n커피: {resources["커피"]} g\n돈 : $ {profit}")
    # choice가 에스프레소 / 라떼 / 카푸치노 중 하나라면
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]        # 이 시점에 drink 변수가 선언된 이유 MENU["off"]
        if is_resources_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["가격"]):
                # 여기까지 실행이 되면 투입된 돈이 더 많다는 의미겠네요.
                # 그러면 돈도 다 들어갔어 다음 단계에 해당하는게 뭐죠?
                # 재료 차감하고 실제로 음료 나와야 합니다.
                # 현재 문제는 에스프레소라면 문제가 생깁니다. 그러면 for문 써가지고 처리해야겠네요.
                # resources["물"] -= drink["재료"]["물"]
                # resources["우유"] -= drink["재료"]["우유"]
                # resources["커피"] -= drink["재료"]["커피"]
                # print(f'{choice}☕가 나왔습니다. 맛있게 드세요 ! ❤️')
                make_coffee(choice, drink["재료"])
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요. ❤️")









