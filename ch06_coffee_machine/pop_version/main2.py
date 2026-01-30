MENU = {
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

resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}
def is_resources_enough(order_ingredients):     # MENU[choice]["재료"]
    """"DocString : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True 반환, 아니면 False 반환
    :param: order_ingredients
    :return: True / False
     """""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다. 🙏")
            return False
    return True

def process_coins():
    """동전 들을 입력 받아 전체 금액을 반환하는 함수 call3() 유형"""
    sum = 0
    sum += int(input('쿼터 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.25
    sum += int(input('다임 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.1
    sum += int(input('니켈 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.05
    sum += int(input('페니 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.01
    return sum

def is_transaction_successful(money_received, drink_cost) :    # 보통 is로 시작하면 bool 타입
    """process_coins()의 결과값과 음료 가격을 매개변수로 삼아 동전이 가격보다 높으면 True / 아니면 False 반환. 그리고 True라면 profit에 음료가격만큼 추가해주고, 잔돈 반환하는 출력문을 작성해야 합니다.
    :params: money_received, drink_cost
    :return: True / False"""
    charge = money_received - drink_cost
    if charge >= 0:
        print(f'잔돈 ${charge}를 반환합니다.')
        global profit
        profit+= drink_cost
        return True
    else:
        print(f'동전이 충분하지 않습니다. 금액 ${money_received}를 반환합니다.')
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료명"]["재료"]들을 차감함.
        -> 차감은 무조건 이루어지겠네요. 돈도 다 있고 재료도 충분했으니까.
    """
    for stuff in order_ingredients:
        resources[stuff] -= order_ingredients[stuff]
    print(f'{choice}☕가 나왔습니다. 맛있게 드세요 ! ❤️')

is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    if choice == "off":
        print("자판기가 종료되었습니다. ⭐")
        is_on = False
    elif choice == "report":
        print(f"물 : {resources["물"]} ml\n우유: {resources["우유"]} ml\n커피: {resources["커피"]} g\n돈 : $ {profit}")

    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["가격"]):
                make_coffee(choice, drink["재료"])
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요. ❤️")