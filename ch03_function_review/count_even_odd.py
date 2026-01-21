# count_even_odd.py
'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개변수 : list numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
# 함수 정의 영역


# 근데 위 내용이 너무 어렵다면 ? ->
numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers에 반복문이랑 조건문 도입해서
'''
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
even_number = 0
odd_number = 0
for num in numbers:
    if num % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

print(f"짝수의 개수 : {even_number}개\n홀수의 개수 : {odd_number}개")


def count_even_odd(numbers):    # 정의할 때 ()내부에 있는거 매개변수다
    even_number = 0
    odd_number = 0
    for num in numbers:
        if num % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    print(f"짝수의 개수 : {even_number}개\n홀수의 개수 : {odd_number}개")

# 함수 호출 영역
count_even_odd([1,2,3,4,5,6,7,8,9,10,11])
'''
argument로 집어넣은 [1,2,3,4,5,6,7,8,9,10,11] 는 def count_even_odd(numbers):로 되어있는
부분으로 넘어갔을 때
numbers = [1,2,3,4,5,6,7,8,9,10,11] 로 대입되기 때문에
함수의 로직 부분에 [1,2,3,4,5,6,7,8,9,10,11] 대신에 numbers를 써야 됩니다.
'''


def calc_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2
    if bmi < 18.5:
        answer = "저체중"
    elif bmi < 23:
        answer = "정상"
    elif bmi < 25:
        answer = "비만 전 단계"
    elif bmi < 30:
        answer = "1단계 비만"
    elif bmi < 35:
        answer = "2단계 비만"
    else:
        answer = "3단계 비만"

    print(f"당신의 bmi 지수는 {round(bmi, 2)}이고 {answer} 입니다.")

calc_bmi(172, 68)
'''
실행 예
당신의 bmi 지수는 22.99이고 정상 입니다.
'''

