# '''
# 응용 예제
# list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3 번째 요소로부터 7 번째 요소만 추출한 결과, 그리고 그 list에서 2 번째 요소를 출력하는 프로그램을 작성하시오. -> index 넘버 관련 부분을 떠올리셔야 합니다.
#
# 실행 예
# 3 번째 요소로부터 7 번째 요소 = [ 30, 40, 50, 60, 70 ]
# 3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40
# '''
# list_origin = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
# # 슬라이싱 개념 리스트명[시작값 : 종료값 : 증감값]
# print(f"3 번째 요소로부터 7 번째 요소 = {list_origin[2:7]}")
# print(f"3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = {list_origin[2:7][1]}")
# # 하지만 원본 list_origin이 그대로 남아있기 때문에 불편할 수 있다면,
# list_sliced = list_origin[2:7]
# print(f"3 번째 요소로부터 7 번째 요소 = {list_sliced}")
# print(f"3 번째 요소로부터 7 번째 요소 = {list_sliced[1]}")
# '''
# 사용자로부터 1에서 12 사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.(윤년은 고려x)
#
# 실행 예
# 1 ~ 12 사이의 월을 입력하세요 >>> 2
# 2월은 28일까지입니다.
# - list를 써도 되고, dictionary를 써도 됩니다.
# '''
# month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))
# # 풀이법 # 1 : 12개 짜리 list 선언 방법
# last_dates = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# print(f"{month}월은 {last_dates[month-1]}일까지입니다.")
# # 풀이법 # 2 : 28, 30, 31 세 개짜리 list를 사용하는 방법
# last_dates_short = [ 28, 30, 31 ]
# # month가 특정 숫자일 때 특정 인덱스를 참조하게끔 하는 조건문 작성
# last_date = 0
# if month == 2:
#     last_date = last_dates_short[0]
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     last_date = last_dates_short[1]
# elif month in [ 1, 3, 5, 7, 8, 10, 12 ]:
#     last_date = last_dates_short[2]
# else:
#     print("잘못입력하셨습니다.")
#     last_date = "X"
#
#
# print(f"{month}월은 {last_date}일까지입니다.")
# # dictionary 사용 방법
# last_date_dict = {
#     1: 30,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31,         # 혹시 뒤에 다시 key-value 를 추가할 수 있기 때문에 ,를 치는게 매너
# }
# print(f"{month}월은 {last_date_dict[month]}일까지입니다.")

'''
https://github.com/maybeags/korit_2026_python_2
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# 비어있는 list / set을 생성
# field_trip_list = []
# field_trip_set = set({})        # 비어있는 set을 만들기 위해서는 set()함수로 {}를 감싸줘야 함.
# print(type(field_trip_set))
# # 학생 수만큼 input()함수가 실행되어야 할 것 같습니다. 그리고 그 결과값을 list / set에 추가해줘야 합니다.
# student_number = 3
# for i in range(student_number):
#     student = input("희망하는 수학여행지를 입력하세요 >>> ")
#     field_trip_list.append(student)
#     field_trip_set.add(student)
#
# print(f"조사된 수학여행지는 {field_trip_list}입니다.")  # 현재 이부분에 추가적인 가공이 필요합니다.
# print(f"조사된 수학여행지는 {list(set(field_trip_list))}입니다.")  # 현재 이부분에 추가적인 가공이 필요합니다.
# print(f"조사된 수학여행지는 {field_trip_set}입니다.")
# 출력문을 작성



'''짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장하세요.
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [5, 10, 15, 20, 25, 30]입니다.
입력 받은 숫자들 중 짝수는 [10, 20, 30]입니다.'''
# 빈 list 선언
numbers = []
numbers_even = []
num = int(input("몇 개의 숫자를 입력할까요? >>> "))
# num만큼 반복문을 돌아서 list에 추가해줘야겠네요.
for i in range(num):
    number = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
    numbers.append(number)          # 입력 받자마자 전부 다 numbers 리스트에 저장
    if number % 2 == 0:             # 입력 받은 숫자가 짝수라면 실행되는 조건문
        numbers_even.append(number) # 그때 numbers_even에 저장
# for i in numbers:
#     if i % 2 == 0:
#         numbers_even.append(i)

print(f"입력 받은 숫자는 {numbers}입니다.")
print(f"입력 받은 숫자들 중 짝수는 {numbers_even}입니다.")
# 입력 받은 숫자들 전체 출력 및 짝수만 출력해야합니다.

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비있는 리스트 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers(last_num)           # call2유형
print(add_numbers2(last_num))    # call4유형    

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
'''