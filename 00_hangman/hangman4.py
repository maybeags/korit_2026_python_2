import random
# 기본 세팅 파트를 좀 같이 작성하겠습니다. maybeags
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


display = []
word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")
for letter in chosen_word:
    display.append("_")
#todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
lives = 6
end_of_game = False

while not end_of_game:
    guess = input("알파벳을 입력하시오 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess


    # todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
    #  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

    '''
        else: 
            lives-=1 으로 쓰시면 안됩니다.
            알파벳을 하나 입력할 때마다 모든 문자에서 알파벳이 맞는지 확인하는 조건문이
            실행되기 때문에(반복문 내부에 if문이 있으니까) 한 번 틀리면 문자열 개수만큼
            lives-=1이 실행됩니다.
            
            이상을 이유로 for 반복문 바깥에서(들여쓰기 적용 x) guess가 chosen_word에
            속하는지 아닌지를 확인하는 추가 조건문을 작성해야 합니다.
    '''
    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives} 번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True                  # 얘가 True로 바뀌었는데
            # break
            print(f"정답은 {chosen_word}입니다.") # 얘가 실행되고 종료되었다는 점입니다.

    # todo - 3 : 사용자가 모든 문자를 맞췄는지 확인하는 조건문을 작성하시오.
    # 다 맞췄다면 "정답입니다 !! ✔️" 를 출력하시오. -> display에 "_"가 없다.
    if "_" not in display:
        print("정답입니다 !! ✔️")
        end_of_game = True          # 얘만 되고 break 쓰면 안되겠네요.


# 정답을 맞췄을 때 어느 부분을 맞췄는지 출력되지 않음.
# stages 리스트 내에 있는 그림이 출력되지 않음.
    print(" ".join(display))
    print(stages[lives])