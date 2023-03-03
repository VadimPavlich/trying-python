birthday = input(
    "Введіть свій день народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")

life_number = sum(int(number) for number in birthday)

while life_number >= 10:
    life_number = sum(int(number) for number in str(life_number))

print("Ваша цифра життя:" + str(life_number))
