# ch07_inheritance -> main
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = [ '구분', '부모 클래스', '자식 클래스']
table.add_row(['의미', '상속 해주는 클래스', '상속 받는 클래스'])
table.add_row(['용어', '슈퍼 클래스', '서브 클래스'])
table.add_row(['', '기반 클래스', '파생 클래스'])
print(table)
'''
+------+----------------------------+------------------------+
| 구분 |    부모 클래스           |   자식 클래스       |
+------+----------------------------+------------------------+
| 의미 | 상속 해주는 클래스 | 상속 받는 클래스  |
| 용어 |    슈퍼 클래스          |   서브 클래스        |
|         |    기반 클래스           |   파생 클래스       |
+------+----------------------------+------------------------+
상속(inheritance)
1. 상속이란 ?
    어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 생성할 수 있는데, 클래스의 기능을 물려 받을 때 '상속 받는다'는 표현을 사용함.
    상속 관계에 있는 클래스를 표현할 때 부모(슈퍼) 클래스 / 자식(서브) 클래스라는 용어를 사용함.
    
2. 상속 관계 구현
    두 클래스가 상속 관계에 놓이려면 IS-A 관계를 성립해야 함. IS-A 관계란 '~은 ~이다'로 해석할 수 있는 관계를 의미. ex) 학생은 사람이다.
    
    *IS-A 원문 : is a kind of -> Dog is a kind of Animal -> '개'는 '동물'의 일종이다.
형식 :
class 슈퍼클래스:
    본문(생성자, 메서드 기타 등등)
    
class 서브클래스(슈퍼클래스):
    본문
'''
class Person:                           # 슈퍼 클래스
    def __init__(self, name):   # 생성자
        self.name = name            # 관련 정보 MenuItem 부분에서 꼭 확인하세요.

    def eat(self, food):                # call2()유형의 매개변수 있고 return 타입 없는 메서드 정의
        print(f'{self.name}이(가) {food}을(를) 먹습니다.')

# 객체 생성
person1 = Person(name='김일')         # keyword argument를 통한 객체 생성
# 메서드 호출
person1.eat('버터 와플')

# 서브 클래스의 정의
class Student(Person):
    def __init__(self, name, school):           # 생성자
        super().__init__(name)              # name이라는 인스턴스 변수는 슈퍼 클래스로부터 상속 받는다는 의미
        self.school = school                    # 슈퍼 클래스에 없는 인스턴스 변수 school은 자기 자신에서 선언 및 초기화

    def study(self):                                    # 매개변수도 없고 return도 없는 call1() 유형으로 정의했습니다.
        print(f'{self.name}은(는) {self.school}에서 공부합니다.')

potter = Student(school='호그와트', name='해리포터')
potter.study()          # 결과값 : 해리포터은(는) 호그와트에서 공부합니다.
potter.eat('고구마')       # Student 클래스에는 없는 부모 클래스의 메서드인 eat()을 호출하는 것이 가능

'''
3. 서브 클래스의 __init__()       : 언더스코어 두 개
서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼 클래스의 생성자를 먼저 호출'하는 코드를 작성 해야만 합니다.

super -> 슈퍼 클래스를 의미(self와 비교되겠습니다). 즉, Student의 생성자를 호출하려면 super().__init__(name)에 의해서 슈퍼 클래스인 Person의 생성자가 먼저 호출되면서 슈퍼 클래스의 객체가 먼저 '생성'됩니다. 이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스 Student로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수를 가진 채로 객체 생성이 되면서 서브 클래스 객체 생성이 완료됩니다.

서브 클래스의 객체 생성 과정 -> 부모 클래스를 기준으로 한 객체가 먼저 생성되고 -> 자식 클래스의 인스턴스 변수와 합쳐져서 -> 서브 클래스의 객체 생성이 완료됨.

이상의 코드에서는 Person 객체가 name 속성 하나만 가지고 있는 상태이기 때문에 활용성이 떨어져 보일 수 있으나 만약에 Person 내부의 속성으로 name, age, address, id 등 다수의 속성을 지니고 있는데 Student에서 별개로 school까지 더해야한다면 상속의 필요성을 확인할 수 있습니다. 또한 eat() 메서드 뿐만 아니라, show_info() 등의 메서드들을 전부 다 가지고 있는데 Student에 별개로 정의해야한다면 너무 귀찮겠죠.

4. 서브 클래스의 인스턴스 자료형
슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
하지만 서브 클래스의 인스턴스는 서브 클래스의 인스턴스 이면서 동시에 슈퍼 클래스의 인스턴스
Student 클래스의 객체는 Student의 인스턴스이면서 동시에 Person의 인스턴스라는 의미입니다.

어떤 객체가 특정한 클래스의 인스턴스인지 아닌지를 확인하기 위해서 사용하는 함수 : isinstance()
형식 :
isinstance(객체명, 클래스명)
'''
print(isinstance(potter, Student))      # 결과값 : True
print(isinstance(potter, Person))       # 결과값 : True

print(isinstance(person1, Person))  # 결과값 : True
print(isinstance(person1, Student)) # 결과값 : False
'''
그래서 그 결과 person1은 study() 메서드를 호출할 수 없지만 potter는 eat() 메서드를 호출할 수 있습니다.
'''










