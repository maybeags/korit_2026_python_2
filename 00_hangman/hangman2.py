import random

word_list = [ "apple", "banana", "camel" ]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")

# list에서 각 요소를 추가하는 방법 ? : 리스트명.append("더할데이터")
#todo - 1 : 비어 있는 list인 display를 만드시오. chosen_word의 각 문자
# 개수마다 "_"를 추가하시오. 예를 들어 chosen_word == "apple"이라면,
# display = [ "_", "_", "_", "_", "_" ]이 되어야 합니다.
display = []            # 비어있는 list인 display를 선언 및 초기화
# 예를 들어 apple이라면 반복이 5 번, banana라면 반복이 6
for letter in chosen_word:
    display.append("_")
print(display)

#todo - 2 : chosen_word의 각 문자들을 반복 시킵니다. 만약 그 위치의 문자가
# guess와 일치하면, 해당 위치의 display에서 해당 문자를 공개하세요.
# ex) 사용자가 "p"를 입력했고, chosen_word가 "apple"이라면
# display = [ "_", "p", "p", "_", "_" ]

# guess 변수를 사용하려면 선언해야 하네요.
guess = input("알파벳을 입력하세요 >>> ").lower()

for i in range(len(chosen_word)):   # 두 개의 for문을 다르게 작성한 이유를 파악하시면 좋습니다
    # list 내의 특정 index 부분을 바꿔야 하기 때문입니다.
    if guess == chosen_word[i]:     # 즉, i가 display의 인덱스로도, chosen_word의 인덱스로도 사용됩니다.
        display[i] = guess          # 그러면 맞춘 부분의 list의 인덱스를 guess 값으로 재대입하겠다는 의미입니다

print(display)