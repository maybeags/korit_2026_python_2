# hangman1.py 파일 생성
import random
# 임의의 단어를 선택해서 가지고 오기 위해서 random import
# 사용 예시
# numbers = [ 1, 2, 3, 4, 5 ]
# for i in range(5):
#     print(random.choice(numbers))
# 우리는 word_list를 만들어서 random.choice()를 호출하여 임의의 단어를
# 꺼내볼 예정입니다.

word_list = [ "apple", "banana", "camel" ]

# print("apple".upper())
# print("APPLE".lower())
# input("알파벳을 입력하세요 >>> ")

#todo - 1 : word_list에서 하나의 단어를 임의적으로 선택하도록 random 모듈을
# 사용하고 해당 단어를 chosen_word 변수에 담으시오.

chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 2 : 사용자에게 알파벳 하나를 추측해서 입력하라고 요청하고, 이를
# guess 변수에 담으시오. 그리고 대문자로 시작하는 경우를 방지하기 위해
# input() 함수 뒤에 .lower() method를 적용하시오.

# .lower()이라고 하는 method는 . 앞이 string
guess = input("알파벳을 입력하시오 >>> ").lower()
print(guess)

#todo - 3 : guess에서 입력한 문자 하나가 chosen_word의 string 문자열
# 중에 하나의 문자와 일치하는지를 반복문을 통해 확인할 수 있도록 프로그램을
# 작성하시오. 맞으면 정답, 틀리면 오답이라고 출력할 수 있도록 할 것.

# string 데이터를 반복문 돌리게 되면 문자 하나씩 빠져나옵니다.
# for i in "apple":
#     print(i)

# 만약 chosen_word가 banana고 guess가 b 라면
'''
정답
오답
오답
오답
오답
오답

만약 chosen_word가 apple이고, guess가 p 라면
오답
정답
정답
오답
오답
'''




# 참고 : 강사 github id : maybeags
# https://www.github.com/maybeags/korit_2026_python_2