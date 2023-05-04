import random

# Запитуємо в користувача розмірність матриці
n = int(input("Введіть розмірність матриці:"))

# Створюємо квадратну матрицю за допомогою спискового виразу
# кожен елемент матриці - це випадкове число в діапазоні [-50, 50]
matrix = [[random.randint(-50, 50) for j in range(n)] for i in range(n)]

# Виводимо вихідну матрицю на екран
for row in matrix:
    print(row)

# Запитуємо в користувача число k
k = int(input("Введіть число k:"))

# Формуємо одновимірний масив, діленням додатніх елементів матриці на k
divided_array = []
for row in matrix:
    for element in row:
        if element > 0:
            divided_array.append(element / k)

# Виводимо отриманий масив на екран
print("\nОтриманий масив:")
print(divided_array)
