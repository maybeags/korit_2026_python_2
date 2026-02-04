# task.py
'''
다음 지시 사항을 읽고 Hybrid 클래스를 구현하시오.

지시 사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.

3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
'''
class Car:
    max_oil = 50        # 클래스 변수
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0 :
            return         # 함수 / 메서드에 return 쓰면 그대로 함수 / 메서드가 종료
        self.oil += oil     # self.oil과 oil이 서로 다른 의미라고 했습니다.
        if self.oil > Car.max_oil:  # 클래스 변수의 값을 초과했다면, 이란 의미이며, 인스턴스 메서드내에서 클래스 변수를 참조하기 위해서는 클래스명.클래스변수명을 작성해야 합니다. cls.클래스변수명이 아니라.
            self.oil = Car.max_oil      # 무조건 50으로 맞춰주겠다는 의미가 되겠네요.

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')

class Hybrid(Car):
    # 특정 클래스 변수가 필요합니다.
    max_amount = 30
    # 객체 생성 방식을 고려한 생성자를 정의해야 함(person1과 potter의 생성 방식에 주목할 것)
    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount
        print(f'하이브리드 차량이 생산되었습니다.')
    # add_oil() 메서드를 부모 클래스에서 호출했을 때 안내문이 없었다는 점에 주목하여 overriding해야합니다.
    def add_oil(self, oil):
        super().add_oil(oil)    # Car의 add_oil을 확인했을 때 self.oil값이 최대 50으로 고정되어있다는 것을 확인했습니다
        print(f'기름을 {self.oil} 주유했습니다.')
    # charge() 메서드의 로직은 add_oil()과 거의 같습니다. 다만 여기도 안내문이 필요합니다.
    def charge(self, amount):
        if amount <= 0 :
            return
        self.amount += amount
        if self.oil > Hybrid.max_amount:
            self.amount = Hybrid.max_amount
        print(f'전기를 {self.amount} 충전했습니다.')
    #hybrid_info()의 경우 현재 주유 상태를 직접 타이핑해도 되지만 부모 클래스의 메서드를 호출하는 방법으로 해결할 수도 있습니다.

    def hybrid_info(self):
        # print(f'현재 주유 상태 : {self.oil}')
        super().car_info()      # overriding을 해야지만 부모 클래스의 메서드를 호출할 수 있는 것은 아닙니다.
        print(f'현재 충전 상태 : {self.amount}')

car = Hybrid(oil= 0, amount=0)
car.add_oil(100)
# print(car.oil)
car.charge(50)
car.hybrid_info()

'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. -> call3()
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 -> call3()
        (넓이 = 너비 * 높이)
3. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.

 
circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.                    # 이건 아무리 봐도 생성자 부분인거같고
이름이 원1인 원의 넓이는 ____ 입니다.                # 얘가 그러면 draw()여야 할 것 같습니다.
원의 넓이 : ____                                                     # 얘가 area() 메서드일 듯
너비가 10, 높이가 8인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'{self.name}')

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {self.radius}인 {self.name}이 생성되었습니다.')

    def draw(self):
        #super().draw()      # 부모 클래스의 메서드 이름만 가져오고 호출 안해도 뭐 그만입니다.
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()}입니다.')

    def area(self):
        # 부모 클래스의 area는 아무 로직이 없지만 여기서 정의하는 것도 가능합니다.
        return 3.14*(self.radius**2)

class Rectangle(Shape):
    #생성자를 위에를 보고 정의하시면 되겠습니다.
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {self.width}, 높이가 {self.height}인 {self.name}이 생성되었습니다.')

    def area(self):
        return self.width*self.height

    def draw(self):
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()}입니다.')

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')
print()
rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')









