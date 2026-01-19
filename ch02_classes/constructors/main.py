'''
1. 생성자(constructor)
'''
# 복습 클래스 정의
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color
    def display_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
# 객체 생성
satang = Candy()
# 메서드를 통해서 shape / color 속성에 값 입력
satang.set_info("구형", "갈색")
satang.display_info()
'''
satang이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형" 모양의 "갈색"이라는 속성(attribute)을 갖게 됩니다.

satang 인스턴스의 생성 과정
    1. 속성값이 없는 인스턴스를 생성
    2. 값을 저장할 수 있는 메서드를 정의하고 호출
    
그렇다면 처음부터 값이 있는 인스턴스를 생성하면 코드라인이 줄어들지 않을까.
    -> 이에 대한 해답이 생성자(constructor)
    C / Java에서는 생성자는 클래스명과 동일합니다(즉 Candy가 생성자가 됩니다)
    JavaScript에서는 constructor라고 그냥 대놓고 생성자라고 합니다.
    근데 유독 python에서만 이상한 방식으로 만드는데
    : __init__()
    
생성자란 ?
    객체를 생성할 때 호출되는 특별한 메서드() -> 메서드가 뭐였는지 복습할 필요가 있겠네요, -> 클래스에 종속된 함수() 였습니다. 호출 방식도 달랐습니다.
    : 함수명() / 객체명.메서드명()
    생성자는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의 초기화(initialization)용도로 사용, 즉 속성에 값이 대입된 상태로 인스턴스를 생성할 수 있습니다.
형식 :
class 클래스명:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
'''
class Candy2:
    def __init__(self, shape, color):   # 여기서 우리는 Candy2()로 만들 수 없고 Candy2(속성값1, 속성값2)로 만들겠다고 정의했기 때문입니다.
        self.shape = shape
        self.color = color

    def display_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
# 객체 생성
# satang2 = Candy2()      # 이렇게 쓰니까 오류가 발생합니다.
satant2 = Candy2("정육면체", "흰색")  # 이렇게 쓰셔야 합니다.
satant2.display_info()
'''
satang / satang2 사이의 인스턴스 생성 방식의 차이를 신경써서 볼 필요가 있습니다.

2. 소멸자(Destructor)
    인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때
    호출되는 메서드. 이를 소멸자라고 하는데, 커스텀하기 위해서 정의하는 메서드는
    __del__()입니다.
'''
class Sample:
    # 생성자 정의
    def __init__(self):
        print("인스턴스가 생성되었습니다.")
    # 소멸자 정의
    def __del__(self):
        print("인스턴스가 소멸되었습니다.")
# 객체 생성
sample = Sample()   # 근데 이러고 실행해보면 좀 특이한 결과를 얻을 수 있습니다.
# 생성자는 객체 생성될 때 호출되는거니까 생성됐다는 안내가 뜨는 것이 이상하지 않지만
# 알아서 인스턴스가 소멸했다고 출력되고 있다는 점에 주목해야합니다.
del sample          # 소멸자를 호출하는 방법(호출 방법이 특이하네요)
print("프로그램이 종료되었습니다.")
'''
sample = Sample()
print("프로그램이 종료되었습니다.")
인스턴스가 생성되었습니다.
프로그램이 종료되었습니다.
인스턴스가 소멸되었습니다.

sample = Sample()
del sample
print("프로그램이 종료되었습니다.")
인스턴스가 생성되었습니다.
인스턴스가 소멸되었습니다.
프로그램이 종료되었습니다.

즉 소멸자를 정의해두고 걔를 호출하면 원하는 시점에 객체를 소멸시킬 수 있다는 의미가 됩니다. 메모리 효율성으로 프로그램이 종료될 때 날리는게 아니라 더이상 사용되지 않을 때 객체를 소멸시킬 수 있다는 것으로 개발자가 객체 생성 시점 및 소멸 시점을 통제할 수 있습니다.


기본 예제
생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.
지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계(객체 생성 단계)에서의 코드
usb = USB(64)
usb.get_info()

실행 예(콘솔에 찍히는 예시)
64GB USB
'''
# 클래스 정의 영역
class USB:
    # 생성자 정의 영역
    def __init__(self, capacity):
        self.capacity = capacity
    # get_info()라고 하는 메서드 정의
    def get_info(self):
        print(f"{self.capacity}GB USB")
        # 이상의 코드와 Candy2 코드를 비교하시면 됩니다.

# 객체 생성 영역
usb = USB(64)       # 여기서 생성자를 호출했고(capacity field에 64를 대입함)
usb.get_info()      # 여기서 64GB USB라는 출력문이 나오는 메서드를 호출함.
'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.
class Service를 정의하고, 생성자를 통해 매개변수 service를 받고,
print() 메서드를 생성자와 소멸자 내에 작성하시오.

main 단계에서의 작성(객체 생성 단계에서의 작성)
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.

- Sample 클래스의 코드를 참조할 것.
'''
class Service:
    # 생성자 정의 영역
    def __init__(self, service):
        self.service = service
        print(f"{self.service} Service가 시작되었습니다.")
    # 소멸자 정의 영역
    def __del__(self):
        print(f"{self.service} Service가 종료되었습니다.")

s = Service("길 안내")
del s
'''
응용 예제
다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시 사항
1. 다음과 같은 방법으로 man / woman 인스턴스를 생성하시오.
man = Person("james")
woman = Person("emily")
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is born.
emily is born.

3. 다음과 같은 방식으로 man 인스턴스를 삭제하시오.
del man

4. 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.

실행 예
james is born.
emily is born.
james is dead.
emily is dead.          # 종료되기 직전에 woman 객체도 삭제되기 때문에 del woman을 하지 않더라도 뜹니다.
'''
# 클래스 정의 영역
class Person:
    # 생성자 정의 영역
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is born.")
    # 소멸자 정의 영역
    def __del__(self):
        print(f"{self.name} is dead.")

# 객체 생성 영역
man = Person("james")   # 이거 호출 했을 때 james is born.이 출력되어야 합니다. 그렇다면 어디에 print()문을 작성해야하는가를 고민해야 하겠네요.
woman = Person("emily")

del man
del woman
print("프로그램이 종료되었습니다.")

# ch02_classes 내부에 functions_review 패키지 생성 -> main.py