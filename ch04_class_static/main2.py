print('뭔가 이상함')
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있도록 Bag 클래스를 정의할 예정입니다. - 객체가 만들어질 때마다 클래스 변수의 개수를 증가시킬 예정.
'''
# 클래스 정의
class Bag:
    count = 0           # 클래스 변수 선언 및 초기화
    def __init__(self):     # 생성자 정의 / 인스턴스 메서드에 해당함 : @가 없으니까요.
        Bag.count += 1   # 객체를 하나 생성할 때마다 클래스 변수인 count가 1씩 증가함.
        print('가방이 생성되었습니다.')   # 근데 cls.count가 아니라 Bag.count인 점에 주목하세요.
        # 인스턴스 메서드가 클래스 변수를 참조할 때는 클래스명.클래스변수명으로 참조함.
        # cls.클래스변수명은 클래스메서드 내에서만입니다.

     # 클래스 메서드 정의
    @classmethod
    def sell(cls):
        print('가방이 팔렸습니다.')
        cls.count -= 1              # 차이점에 주목하셔야 합니다.

# 객체 생성 전에 가방 재고를 확인하겠습니다.
print(Bag.count)        # 결과값 : 0
# 그런데 클래스메서드의 특징상, 객체를 안만들어도 호출이 가능하다는 점 때문에
Bag.sell()
print(Bag.count)        # 결과값 : -1
# 객체를 생성해보겠습니다.
bag1 = Bag()        # 생성자 내에 저희가 아무런 인스턴스 변수를 정의하지 않았기 때문에
# 오랜만에 이렇게 뻥 비어있는 객체 생성했습니다.
print(Bag.count)
bag2 = Bag()
print(Bag.count)
Bag.sell()
print(Bag.count)
'''
이상의 코드에서 이제 주목하셔야 할 점은 class 하나를 정의하는데 저희는 생성자도 배웠고, 인스턴스메서드도 배웠고, 그 내부에 인스턴스 변수도 있고, 클래스 변수와 클래스 메서드와 정적 메서드가 다 정의될 수 있다는 점입니다.

수업 상황이기 때문에 분할해서 작성하고 나누었지만 실무 상황에서는 어떻게 여러 가지로 작성될 지 알 수 없습니다.

클래스 변수 / 클래스 메서드 활용 예제
지시 사항
1. Shop 클래스는 다음과 같은 클래스 변수를 가지고 있다
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 가지는 리스트
    
    menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales("떡볶이", 1)       # 떡볶이을(를) 1개 판매
Shop.sales("김밥", 2)        # 김밥을(를) 2개 판매
Shop.sales("튀김", 5)        # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.get_total()} 원")
'''
class Shop:
    # 지시 사항에서 어떤 부분이 클래스 변수이고, 어떤 부분이 클래스 메서드인지,
# 그리고 걔네가 어떤 방식으로 호출되는지, 결과값은 어떻게 되는지를 지시 사항을 읽고 감을 잡아보도록하겠습니다.
    # 클래스 변수들
    total = 0
    menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]
    # 전체적으로는 list인데 내부 element는 key가 메뉴명이고 value가 가격인 dict

    # 클래스 메서드
    # print(f"매출 : {Shop.get_total()} 원")       # return이 존재한다
    @classmethod
    def get_total(cls):
        return cls.total # 뭐라고 쓸지 클래스 변수 참조하는 법 아셔야 합니다.

    @classmethod
    def sales(cls, menu_name,  quantity):
        # menu_list를 기준으로 list의 내부 element를 확인하는 방법이 뭐였는지 : 반복문
        for menu_dict in cls.menu_list: # 메뉴 리스트이 내부는 dictionary들이니까
            # dictionary 반복문 돌리면 뭐가 튀어나왔었나요?
            # dictionary의 value를 확인하는 방법이 무엇이었는지 떠올리셔야 합니다.
            if menu_name in menu_dict:      # menu_dict의 key 중에 menu_name과 겹치는게 있다면
                cls.total += menu_dict[menu_name] * quantity
                print(f'{menu_name}을(를) {quantity}개 판매')



print(f"매출 : {Shop.get_total()} 원")
Shop.sales("떡볶이", 1)       # 떡볶이을(를) 1개 판매
Shop.sales("김밥", 2)        # 김밥을(를) 2개 판매
Shop.sales("튀김", 5)        # 튀김을(를) 5개 판매
print(f"매출 : {Shop.get_total()} 원")

dict_example = {"name" : "김영", "age": 20, "address": "부산광역시 부산진구"}
for key in dict_example:
    print(key)