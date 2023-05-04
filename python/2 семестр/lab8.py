import random

m = int(input("Введіть розиірність матриці (m): "))
n = int(input("Введіть розиірність матриці (n): "))
a = int(input("Введіть початок діапазону рандомних чисел:"))
b = int(input("Введіть кінець діапазону рандомних чисел:"))

matrix = [[random.uniform(a, b) for j in range(m)] for i in range(n)]
print("Початкова матриця:")
for row in matrix:
    print(row)

for j in range(m):
    matrix[j][0], matrix[j][m-1] = matrix[j][m-1], matrix[j][0]

print("Кінцева матриця:")
for row in matrix:
    print(row)
