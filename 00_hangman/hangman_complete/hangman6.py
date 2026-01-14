# hangman_complete -> hangman6
# hangman_art.py / hangman_word_list.py
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