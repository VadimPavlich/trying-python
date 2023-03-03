import math

a = float(input("a ="))
b = float(input("b ="))
angle = float(input("angle:"))
angle = round(math.sin(math.radians(angle)), 1)

S = (1/2)*a*b*angle

print(S)

