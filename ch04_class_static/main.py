'''
1. 클래스 변수
    인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스 마다 서로 다른 값
        접근 방식 - 인스턴스 접근(o) / 객체명.변수명
                 - 클래스 접근(x)
    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(o) / 클래스명.클래스변수명
'''
# 클래스 변수 예제
class Korean:
    # 클래스 변수
    country = "한국"

    # 인스턴스 변수 정의
    def __init__(self, name, age, address):
        self.name = name            # 인스턴스 변수 1
        self.age = age              # 인스턴스 변수 2
        self.address = address      # 인스턴스 변수 3

    def show_info(self):
        print(f'제 이름은 {self.name}이고, 나이는 {self.age}살이고, {self.address}에 살고 있습니다.')
# 객체 생성
man1 = Korean(age=20, address="부산광역시 부산진구", name="김일")
man2 = Korean("김이", 22, "서울특별시 종로구")
# 인스턴스 메서드 호출
man1.show_info()    # 제 이름은 김일이고, 나이는 20살이고, 부산광역시 부산진구에 살고 있습니다.
man2.show_info()    # 제 이름은 김이이고, 나이는 22살이고, 서울특별시 종로구에 살고 있습니다.

# 클래스 변수 확인 방법
print(man1.country) # 한국
print(man2.country) # 한국    객체명.클래스변수명 으로 호출 가능
print(Korean.country)   # 한국 클래스명.클래스변수명 으로 호출 가능
# 클래스 변수와 클래스 메서드 때문에 객체명.메서드명 / 클래스명.메서드명인지를 구분하기 위해서는
# Pascal case / snake case인지를 구분해야만 합니다.

'''
객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 합니다. 하지만 클래스 내부의 코드를 보기 전까지는 country가 클래스 변수인지 인스턴스 변수인지를 판단할 수가 없습니다. 이상을 이유로 클래스 변수를 확인하고자 할 때는 클래스명.클래스변수명을 통해서 참조하는 것이 바람직합니다.

클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
class Korean2:
    country = "대한민국"        # 클래스 변수 선언 및 초기화

    # 클래스 메서드 정의하는 방법
    @classmethod        # 이렇게 적어줘야 메서드 정의 시에 self가 자동완성 되지 않습니다.
    def trip(cls, travelling_site):         # 클래스 메서드의 첫 번째 매개변수는 cls입니다. not self
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

# 클래스 메서드의 호출
Korean2.trip("대한민국")
Korean2.trip("미국")
'''
그러면 여태까지와 달리 객체명.메서드명()이 아니라 클래스명.메서드명()으로 호출했다는 사실을 알 수 있습니다. 또한 -> 객체가 아예 생성되지 않았음에도 호출이 가능하다는 특징도 확인할 수 있습니다.

3. 정적 메서드(static method) - Java 배우신 분들은 혼란스러울 수 있는데 Java의 static method는 python에서 class method / static method를 합친 개념입니다.

    : 정적 메서드 또한 self를 쓰지 않습니다. 근데 cls도 안씁니다. -> 인스턴스 변수에 접근하여 사용하는 것이 불가능합니다.
    인스턴스를 생성하지 않아도 사용할 수 있음.
    
    특징 :
        1) 인스턴스 또는 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 # 1
        4) 반드시 작성해야 할 매개변수(self, cls)가 없음 -> 클래스 메서드와의 차이점 # 2

정적 메서드는 self / cls를 둘 다 사용하지 않기 때문에 인스턴스 변수 / 클래스 변수를 모두 사용하지 않는
메서드를 정의할 때 적합합니다. 
정적 메서드는 클래스에 속해있지만 인스턴스(객체)에는 영향을 주지도 않고, 받지도 않습니다.
'''
class Korean3:
    country = '남한'

    @staticmethod           # 정적 메서드 선언
    def slogan():               # self / cls가 자동생성되지 않았습니다. 클래스/인스턴스 변수를 참조하지 않는다는 의미로 볼 수 있습니다.
        print(f'Imagine Your Korea ! ❤️')

    @classmethod
    def trip(cls, travelling_site):
        if cls.country == travelling_site:
            print('국내여행입니다.')
        else:
            print("해외여행입니다.")

# 객체 생성하지않고 호출
Korean3.slogan()
# Korean3.country('미국')

'''
main2.py
















'''