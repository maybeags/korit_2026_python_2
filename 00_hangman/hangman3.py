import random
'''
"".join(반복가능객체) method : . 앞에 있는 문자열을 기준으로 반복 가능 객체의
요소들을 합쳐서 string 형태로 반환함.
'''
temp = [ "안", "녕", "하", "세", "요" ]
hello = "".join(temp)       # 그럼 얘는 공백없이 합치겠다는 의미겠네요
print(hello)
print(type(hello))
hello = "/".join(temp)      # list 요소 사이에 합칠 때 "/"를 추가하겠다
print(hello)

# todo - 1 : "_"가 적용되는 display list 선언하겠습니다.
display = []
word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
for letter in chosen_word:
    display.append("_")

# todo - 2 : 사용자가 guess를 반복할 수 있도록 while 반복문을 작성하겠습니hangman2까지는 guess가 한 번만 실행됐었습니다. 이번에 구현할 부분은 chosen_word의 모든 문자열들을 다 맞췄을 때, 즉, display 내에 "_"가 하나도 없을 때 반복문이 멈추도록 작성할겁니다. 반복문 종료 후에 print("정답입니다!")를 출력하도록 작성하시오.

# 1. input() 함수가 실행되는 곳은 while 반복문 내부여야 합니다
# -> 여러번 알파벳 입력할거니까
# 그렇다면 특정 시점에 반복문을 탈출할 수 있어야 합니다.

while "_" in display:   # display list 내의 요소로 "_"가 있으면 True
    guess = input("알파벳을 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)          # print()의 위치가 for문 내에 있는지

# display에 "_"가 없다면 while 반복문을 탈출하게 됩니다.
# 그런데 print(display)를 확인했을 때 list의 형태로 출력되네요.
# 아까 위에 배웠던 .join()을 활용하여
# a p p l e 로 출력될 수 있도록 반복문 바깥에 print()문을 작성하시오.
print(" ".join(display))    # 한칸 씩 띄우게 했으니까 " ".join



# ctrl + alt + s 누르면 설정 갑니다. 좌측 Editor 선택 -> General 선택 -> soft-wrap 부분 활성화하시면 전체 적용됩니다.
