n = int(input("Введіть ваш варіант: "))
S = 0

for i in range(1, n+11):
    p = i * (1 + i ** 2) / (1 + i ** 2)
    S += p

print(round(S, 1))
