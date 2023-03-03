import math

a = -1.25
b = -1.5
c = 0.75

x = -1.5

while x <= 3.5:
    if x >= 0:
        print('y не існує')
    else:
        y = 10 ** -2 * b*c/x + math.sqrt(a ** 3*x)
        print(round(y, 1))
    x += 0.5
