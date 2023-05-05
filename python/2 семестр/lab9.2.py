import datetime

# Словник, де ключ - ім'я та прізвище учня, а значення - дата його народження
students = {
    "Іваненко Іван Іванович": (2005, 3, 12),
    "Петренко Петро Петрович": (2006, 5, 20),
    "Дубенок Сидір Сидорович": (2005, 4, 8),
    "Коваленко Олександр Миколайович": (2006, 3, 28),
    "Морозова Анна Вікторівна": (2005, 5, 15),
    "Мирний Олег Володимирович": (2006, 4, 3),
    "Добрий Василь Олександрович": (2005, 4, 20),
    "Мала Катерина Олександрівна": (2006, 5, 5),
    "Литвиненко Ілля Олегович": (2005, 3, 30),
    "Боданрчук Максим Вікторович": (2006, 4, 16),
}

# Отримуємо поточну дату
today = datetime.date.today()

# Проходимося по ключах словника та перевіряємо, чи є сьогодні день народження
for name, date_of_birth in students.items():
    year, month, day = date_of_birth
    dob = datetime.date(year, month, day)
    if dob.month == today.month and dob.day == today.day:
        print(name)
