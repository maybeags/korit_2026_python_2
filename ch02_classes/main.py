# ch02_classes / main.py

'''
1. 클래스 도입의 필요성
매개 변수가 6 개인 함수를 하나 예시로 정의하겠습니다.
'''
def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)
# 그리고 얘를 호출하려고 하면
student_info("김일", "컴공", "제임스", "010-1234-5678", "서울특별시 종로구", 4.5)
'''
지금까지 배운 함수와 매개변수, 그리고 호출 시의 매개변수를 통해 함수 하나에 6개의 정보를 전부 저장했습니다. 하지만 만들어야 할 변수의 개수가 이렇게 많다면 100 명의 학생을 저장하려면 600 개의 변수를 처리해야합니다.

이상의 상황(변수에 각각 데이터를 저장한 후에 함수 호출 시 사용)을 벗어나기 위해 클래스와 객체 개입을 도입할 수 있습니다.

class 란? : 객체를 만드는 도구 / 설계도 / 틀 / 청사진(blue print)

    자동차 설계도 -> 클래스
    설계도를 통해 생성된 자동차들 -> 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
    마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있습니다.
    
    인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
    
    클래스는 기본적으로 속성 + 행위 로 이루어져 있습니다.
    속성 : 해당 클래스가 가져야 할 요소들
    행위 : 그 클래스의 객체들이 할 수 있는 것들의 모음
    
형식 :
class 클래스명(얘는 대문자로 시작합니다):
    본문
------------------------------------
객체 생성 방식 :
객체명 = 클래스명()
'''
# 클래스 정의 형식 예시
class WaffleMachine:    # 클래스명은 대문자로 시작하고, Pascal Case로 표기함. 변수는 snake case를 썼었습니다.
    pass                # 나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음.

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle)   # 결과값 : <__main__.WaffleMachine object at 0x00000212A8E030E0>

'''
print(waffle)을 실행시켰을 때의 결과값을 주목해보면, waffle은 WaffleMachine의 객체임을 확인 할 수 있음.

클래스의 구성
1. 객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닙니다.
    - 값 / 기능
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 구분됨.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
        2) 인스턴스 변수 : 인스턴스 들이 개별적으로 가지는 변수
    메서드는
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드

    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줍니다.
    인스턴스 메서드 : 인스턴스 변수를 **사용**하는 메서드
        인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동작됩니다.
        인스턴스 메서드는 첫 번째 매개변수로 self를 추가해야합니다.
'''
# 클래스 정의
class Person:
    def set_info(self, name, age, tel, address):    # 클래스 내부에 def를 정의하면 걔는
        self.name = name                            # function이 아니라 method라고 합니다.
        self.age = age
        self.tel = tel
        self.address = address      # self.속성명 -> 객체에게 특정 속성명을 지니게끔 함.
                                    # self는 아직 생성되지 않은 임의의 객체이름을 의미합니다.
    def show_info(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"연락처 : {self.tel}")
        print(f"주소 : {self.address}")
        '''
        show_info2()를 Person 클래스에 정의하시오.
        호출 방식
        person02.show_info2()
        실행 예
        제 이름은 _____ 이고, ____ 살입니다.
        연락처는 ____ 인데, ____ 에 살고 있습니다.
        내년에는 ____ + 1 살이 됩니다.
        '''
    # show_info2()와 show_info3()는 호출 방법이 좀 다릅니다.
    def show_info2(self):
        print(f"제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.address}에 살고있습니다.\n내년에는 {self.age + 1}살이 됩니다.")

    def show_info3(self):
        return f"제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.address}에 살고있습니다.\n내년에는 {self.age + 1}살이 됩니다."

# 객체 생성
person01 = Person()
print(person01)
person01.set_info("김영", 21, "010-9876-5432", "부산광역시 부산진구")
person01.show_info()
# 클래스에서 정의한 method 사용 -> 메서드 호출 방식 객체명.메서드명() / 함수 호출은 함수명() 이었습니다.
# 속성값 호출 방식
print(person01.name)    # person01 객체의 name이라는 field값을 출력하라는 의미

# person02 객체를 생성하시고, person02.set_info()를 활용하여 여러분 이름 / 나이 / 연락처 / 주소를 입력
# person02.show_info() 메서드를 호출하여 콘솔창에 출력하시오.

person02 = Person() # 객체 생성 과정
# 객체의 속성들에 여러분 이름 등을 입력하는 메서드 호출
# 입력한 정보를 호출하는 메서드 호출
person02.set_info(address="부산광역시 연제구", age=39, name="안근수", tel="010-7445-7113")
# 이상의 방식은 keyword argument라고 합니다. person01의 경우 정의된 순서대로 데이터를 넣어야 하지만
# keyword argument를 적용하면 순서에 상관없이 입력 가능합니다.
person02.show_info()
print("show_info2()")
person02.show_info2()
print("show_info3()")
person02.show_info3()   # 이건 콘솔창에 안찍힙니다.
print(person02.show_info3() + " python 공부가 힘들어요.")
introduction = person02.show_info3()            # 메서드 호출 결과를 변수에 저장
print(introduction)

# 특정 함수/메서드의 호출 결과를 변수에 담은 다음 다른 함수/메서드의 매개변수로 사용하고,
# 또 그 결과가 다시 변수에 저장되는 이 흐름을 함수형 프로그래밍(Functional Programming)이라고 합니다.

# 그리고 객체의 인스턴스 변수(속성)도 '변수'이기 때문에 값을 바꿀 수 있습니다.
person02.name = "카리나"   #객체명.속성명 = "바꿀데이터값"
person02.show_info2()

'''
show_info2()를 Person 클래스에 정의하시오.
호출 방식
person02.show_info2()
실행 예
제 이름은 _____ 이고, ____ 살입니다.
연락처는 ____ 인데, ____ 에 살고 있습니다.
내년에는 ____ + 1 살이 됩니다.




클래스 - 속성 / 행위(method) / 객체 생성 방식 / 객체 속성의 값 변경 방법
    - 특히 method 내에서 여러 제어문(반복문/명령문 등)의 활용을 통해 로직을 작성할 수 있으면 class 파트의 수업을 이해했다고 볼 수 있겠습니다.
    
응용 예제 

다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요 -> 객체도 생성하고, 실행 예를 구현하세요.
1. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.

book1 = Book()
book2 = Book()

2. set_info(self, title, author)를 통해 책 제목을 입력하세요.

3. display_info()를 통해 실행 예와 같이 출력되도록 작성하세요.

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리    
'''
# 클래스 정의
class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"책 제목 : {self.title}\n책 저자 : {self.author}"

# 객체 생성
book1 = Book()
book2 = Book()

book1.set_info(author="민경태", title="파이썬")
book2.set_info("어린왕자", "생텍쥐페리")

print(book1.display_info())
print(book2.display_info())








