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
        "재료": {
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

def is_resources_enough(order_ingredients):
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
        print(is_resources_enough(drink["재료"]))
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요. ❤️")