import random


def field_of_wonders():
    words_for_game = [
        "apple", "phone", "car", "porsche",
        "banana", "city", "girl", "house",
        "laptop", "maserati", "moon", "sun"
    ]

    game_word = random.choice(words_for_game)

    hidden_word = "*" * len(game_word)

    user_input_attempts = int(input("Enter the number of attempts: "))

    correct_letter = set()

    while user_input_attempts > 0:
        print("Hidden word:", hidden_word)
        guess = input("Enter letter: ").lower()
        if guess.isalpha():
            if len(guess) == 1:
                if guess in game_word:
                    print("You found a letter!")
                    user_input_attempts += 1
                    correct_letter.add(guess)
                    hidden_word = "".join(
                        char if char in correct_letter else "*" for char in game_word
                    )
                    if hidden_word == game_word:
                        print("Congratulations! You guessed the word!")
                        break
                else:
                    print("Wrong letter.")
            elif guess == game_word:
                print("Congratulations! You guessed the word!")
                break
            else:
                print("Incorrect guess. Try again.")
        else:
            print("Please enter a letter or word. Not number etc.")
            break
        user_input_attempts -= 1

    if user_input_attempts == 0:
        print("You have no more attempts left. The end.")


field_of_wonders()
