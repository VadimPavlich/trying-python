

counter = 1000

while counter:
    if counter % 2 == 1:
        print("odd number:", counter)

    elif counter % 2 == 0:
        print("even number:", counter)

    else:
        print(0)

    counter -= 1


print(counter)
