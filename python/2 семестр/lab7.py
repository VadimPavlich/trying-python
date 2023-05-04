import random
m = int(input("Введіть кількість символів, яку ви хочете вивести:"))
k = int(input("Введіть кількість символів у рядку:"))

for i in range(m):
    num = random.randint(-10, 10)
    print(num, end=" ")
    if (i + 1) % k == 0:
        print()
