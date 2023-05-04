beatles = []

print("Step 1:", beatles)

beatles.extend(("Джона Леннон", "Пол Маккартни", "Джордж Харрисон"))

print("Step 2:", beatles)

names = []

length = int(input("How many artists do you want to add:"))

for i in range(length):
    name = input("Write down who was in beatles:")
    if name == "0":
        break
    names.append(name)

beatles.extend(names)


print("Step 3:", beatles)

del beatles[-1]
del beatles[-1]

print("Step 4:", beatles)

beatles.insert(3, 'Ринго Старр')

print("Step 5:", beatles)
