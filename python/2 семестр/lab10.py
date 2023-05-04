import random

def play_guessing_game():
    secret_number = random.randint(1, 1000)
    print("У мене є число між 1 та 1000. Відгадайте і введіть ваше число...")

    while True:
        user_guess = int(input("Ваше число: "))

        if user_guess == secret_number:
            print("Чудово! Ви вгадали число!")
            play_again = input("Будете грати далі? (введіть 'так' або 'ні'): ")
            if play_again.lower() == "так":
                play_guessing_game()
            else:
                print("Дякуємо за гру. До побачення!")
                break
        elif user_guess < secret_number:
            print("Занадто мале. Спробуйте ще раз.")
        else:
            print("Занадто велике. Спробуйте ще раз.")

play_guessing_game()
