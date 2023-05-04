import random

# Введення значень n, a та b з клавіатури
n = int(input("Введіть кількість елементів списку: "))
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))

# Генерація списку псевдовипадкових чисел на інтервалі [a, b]
lst = [random.uniform(a, b) for i in range(n)]

# Виведення вхідних даних та елементів списку
print("n = ", n)
print("a = ", a)
print("b = ", b)
print("Список: ", lst)

# Знаходження номера мінімального за модулем елемента
min_index = 0
for i in range(1, n):
    if abs(lst[i]) < abs(lst[min_index]):
        min_index = i
print("Номер мінімального за модулем елемента: ", min_index)

# Обчислення суми модулів елементів, розташованих після першого від'ємного елемента
sum_abs_after_negative = 0
found_negative = False
for elem in lst:
    if elem < 0:
        found_negative = True
    elif found_negative:
        sum_abs_after_negative += abs(elem)
print("Сума модулів елементів, розташованих після першого від'ємного елемента: ",
      sum_abs_after_negative)
