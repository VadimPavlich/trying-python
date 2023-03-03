import math

n = int(input('Введіть число n: '))
x = 0
S = 0

for i in range(0, n+10):
    x = math.sqrt(i)/(math.sqrt(i+1)-math.sqrt(i))
    S += x
print(round(S, 1))
