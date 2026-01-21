# hangman_complete -> hangman6
# hangman_art.py / hangman_word_list.py

def play_hangman():
    import random
    import hangman_word_list
    import hangman_art

    display = []
    chosen_word = random.choice(hangman_word_list.word_list)
    for letter in chosen_word:
        display.append("_")
    lives = 6
    end_of_game = False
    print(hangman_art.logo)
    while not end_of_game:
        guess = input("알파벳을 입력하시오 >>> ").lower()

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        if guess not in chosen_word:
            lives -= 1
            print(f"당신의 기회는 {lives} 번 남았습니다.")
            if lives == 0:
                print("모든 기회를 잃었습니다.")
                end_of_game = True
                print(f"정답은 {chosen_word}입니다.")

        if "_" not in display:
            print("정답입니다 !! ✔️")
            end_of_game = True

        print(" ".join(display))
        print(hangman_art.stages[lives])


# play_hangman()
# play_hangman()
# play_hangman()

# 이상과 같이 작성하면 행맨 게임이 3 번 알아서 실행되겠습니다. 전체 코드 목록을 3 번 복사하는 것보다는 효과가 있겠네요.

# 매번 게임이 끝날 때 마다 진행할건지를 물어보고, no 라고 입력하면 게임이 정지되게끔 함수를 반복문으로 감쌀 수도 있겠습니다.

answer = "yes"
while answer == "yes":
    play_hangman()
    answer = input("게임을 계속하시겠습니까?(yes / no) >>> ")

print("게임이 종료되었습니다.")