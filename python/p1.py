income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * (18/100) - 556.2
elif income > 85528:
    tax = income - 14839.2
elif income <= 3090:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


c0 = int(input("Enter c0: "))

while c0 != 1:
    if c0 % 2 == 1:
        c0 = 3*c0 + 1
        print(c0)
    else:
        c0 /= 2
        print(c0)
