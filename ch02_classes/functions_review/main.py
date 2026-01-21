# functions_review / main.py 생성
'''
1. 함수의 정의 : 특정 작업을 수행하는 코드 블록을 정의하는 방법
예를 들어 저희는 turn_right()를 정의했었습니다.

함수 정의 방식(근데 클래스 내부에 들여쓰기 되어있으면 얘는 method네요)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

함수 호출 방식
turn_right()

2. 함수의 종류
    1) 파이썬 내장 함수 (print() / input() / type() / etc...)
    2) 메서드(method)
    3) 사용자 정의 함수

3. 함수 용어 정리(멘토 파이썬에 있습니다)
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 전달 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값(return값) : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미

4. (사용자) 함수의 형식 :
def 함수_이름(매개변수1, 매개변수2):
    실행문

변수 = 함수_이름(argument1, argument2)
'''
# 함수 정의
def write_name(name):   # 정의할 때 소괄호 내에 있는 것을 매개변수라 합니다.
    print(f"당신의 이름은 {name}입니다.")

# 함수 호출
write_name("김영")    # 호출할 때 소괄호 내에 있는 것을 argument라고 합니다.
title = "김일"
write_name(name= title)   # 여기서 argument가 title인 애가
# 이상의 keyword argument를 적용하게 되면 title에 있는 데이터를 name 변수에 저장하겠다는
# 의미가 되기 때문에 특히 매개변수 =/= argument라는 점이 증명되겠네요.
'''
write_name() 함수의 정의 영역에서 name = title로 변경되어서
    print(f"당신의 이름은 {name}입니다.")
를 호출할 때 당신의 이름은 김일입니다. 로 바뀝니다. 즉 argument =/= 매개변수
'''

def write_name_age(name, age): # 매개 변수가 두 개
    print(f"당신의 이름은 {name}이고, 당신의 나이는 {age}살입니다.")

write_name_age("김일", 21)# 그러면 호출할 때 argument도 두 개 여야만 합니다.

'''
우리가 예를 들어서 input("이름을 입력하세요 >>> ")을 이용해서 name이라는 변수에 담았다고 가정하면
name = input("이름을 입력하세요 >>> ")이라고 작성해왔습니다.
즉, 저희는 여태까지 함수의 결과값을 변수에 담아왔었습니다.

파이썬 내장 함수는 이미 함수가 정의되어있고, 개발자들은 함수 호출만 잘 하면 됩니다.
사용자 정의 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 볼 수 있겠습니다.

내장 함수 예시 :
print() / type() / int() / float() / input() / etc...

2. 메서드(method) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는 함수. 사실상 함수와 메서드는 동일한 개념이지만, 호출 방식에서의 차이가 있습니다.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# eng_name = input("당신의 이름을 소문자로 입력하세요 >>> ").upper()
# # 이상의 코드에서 input()은 함수, .upper()는 메서드
#  # print()는 함수   예를 들어 ahngeunsu라고 입력했으면 결과는 AHNGEUNSU
# eng_name2 = input("당신의 이름을 소문자로 입력하세요 >>> ").title()
#
#
# print(eng_name)
# print(eng_name2)

# eng_name3 = input("당신의 이름을 소문자로 입력하세요 >>> ")
# eng_name_upper = eng_name3.upper()
# eng_name_title = eng_name3.title()
# print(eng_name_upper)
# print(eng_name_title)
# 이러면 입력 한 번만 받고 결과값은 두 개 나오겠네요.

'''
함수(메서드)의 유형
'''
# 매개변수 x / 리턴 x
def call1():
    print("[ x | x ]")
# 매개변수 o / 리턴 x
def call2(str_type):
    print("[ o | x ]")
    print(f"{str_type}이라고 입력하셨나봅니다.")
# 매개변수 x / 리턴 o
def call3():
    print("[ x | o ]")
    return "call3()유형입니다."
# 매개변수 o / 리턴 o
def call4(str_type):
    print("[ o | o ]")
    return f"제 이름은 {str_type}입니다."
call1()
call2("안녕하세요.")
call3()
# 이상의 코드 결과값 : [ x | o ]
print(call3())       # 여기서 알 수 있는 것은 print()함수는 return되어있는 부분을 콘솔에 찍어주네요
# 이상의 코드 결과값 :
'''
[ x | o ]
call3()유형입니다.
'''
print(call4("김사"))
name5 = call4("김오")     # 함수의 결과를 변수에 대입한 다음에
print(name5)             # 변수를 출력하는 출력문 작성
'''
call3() / call4() 유형에서 함수 내에 print()를 호출하면 main 단계에서(들여쓰기 안하는 부분에서) print()함수를 따로 호출할 필요가 없어서 훨씬 편할 것 같은데 왜 굳이 return 형태로 입력해서 일일이 print()를 써야하는가라는 문제가 있습니다.
'''
def print_age1(age):
    print(f"제 나이는 {age}살입니다.")

def print_age2(age):
    print(f"제 나이는 {age}살입니다.")
    return age

print_age1(20)
print(f"내년에는 {print_age2(20) +1} 살이 됩니다.")
next_age = print_age2(20)+1
print(next_age)
'''
이상의 예시에서처럼 함수 내부에서 print() 함수를 호출해버리면 argument로 받은 데이터를 편집하는 것이 불가능합니다.

함수형 프로그래밍으로 작성을 하기 위해서는 return 구문을 쓰는 것이 훨씬 더 데이터의 조작 측면에서 편리합니다.


700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈을 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1-4() 중에 어떤 유형을 써야할지 고려하시오)
- 함수 이름 : vending_machine()
- 매개 변수 : 정수 money(이때 call1-4() 중에 하나가 확정되겠습니다)

코드 구성
def vending_machine(필요한 부분 작성하시오):
    필요한부분 작성하시오
    
main 단계(함수호출단계)
vending_machine(3000)

콘솔 실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''
# def vending_machine():
#     pass

# vending_machine(3000)
'''
이상의 메서드를 구현하는 데에 있어서 다양한 부분을 고려해야 합니다. 일단 반복횟수를 결정해야하는데, 3000원을 argument로 집어넣었다고 했을 때
반복이 0-4까지 다섯번 이루어져야합니다. 그런데 3000/7은 4.xxxx로 float 자료형이 튀어나오기 때문에 반복횟수를 고정하기가 힘들 것 같습니다.
여기부터 여러분들이 고민하셔야 합니다.
'''
print(5/2)
print(5//2)

'''
제가 보통 함수 / 메서드를 작성할 때는 main 단계에서 굴러가는지를 먼저 체크합니다.
'''
my_money = 3000
drink_price = 700
# for 반복문을 돌려서 실행 예 처럼 나오도록 하려면 어떡해야 할까요? -> print(f"")
# charge = my_money - (drink_price * 0)
# charge = my_money - (drink_price * 1)
# charge = my_money - (drink_price * 2)
# charge = my_money - (drink_price * 3)
# charge = my_money - (drink_price * 4)

# 윗부분들이 출력이 되어야하는데 0 ~ 4 까지 바뀌는 것을 보니 반복문을 적용할 수 있을 것 같습니다.
print(my_money//drink_price)        # 결과값이 4입니다. 그러면 0 1 2 3 해서 네 번 반복이 돌아가겠네요.
# 이상의 결과를 고려했을 때 in range()에서 + 1 해줘야합니다.
print(int(my_money/drink_price))
for i in range(my_money//drink_price + 1):
    print(f"음료수 = {i}개, 잔돈 = {my_money-(drink_price*i)}")

# main 단계에서 함수화를 어떻게 시킬까를 고민하겠습니다.
def vending_machine(money):
    for i in range(money // 700 + 1):
        print(f"음료수 = {i}개, 잔돈 = {my_money - (700 * i)}")

print("이하는 함수 호출 부분입니다.")
# 함수 호출
vending_machine(3000)


def vending_machine2(money, price):
    for i in range(money // price + 1):
        print(f"음료수 = {i}개, 잔돈 = {my_money - (price * i)}")

# 함수 호출
print("함수 호출2 부분입니다.")
vending_machine2(3500, 700)         # 음료 가격도 우리가 정할 수 있도록 수정했습니다.


'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름 : multiply()
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
...
3 x 9 = 27
'''

# dan = int(input("몇 단을 출력하시겠습니까? >>> "))
# for i in range(1, 10):
#     print(f"{dan} x {i} = {dan*(i)}")


# 이상의 코드를 통해서 main 단계에서 구구단을 작성할 수 있었습니다.
def multiply(n):
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")

# main 부분에서 입력받았습니다.
# dan = int(input("몇 단을 입력하시겠습니까? >>>"))

multiply(3)   # input 함수의 결과값을 int 함수를 통해 자료형을 str에서 int로 바꾸고, 이를 multiply의 argument로 사용한 함수형 프로그래밍








