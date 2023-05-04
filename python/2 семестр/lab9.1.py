text = input("Введіть текст: ")
text = text.lower()  # замінюємо великі літери на малі
print(text)

words = text.split()  # розділяємо текст на окремі слова
longest_word = max(words, key=len)  # знаходимо найдовше слово
print("Найдовше слово: ", longest_word)

vowels = "аеєиіїоуюя"
consonants = "бвгґджзйклмнпрстфхцчшщ"
words = text.lower().split()

# Функція, що рахує кількість приголосних літер у слові


def count_consonants(word):
    return sum(1 for letter in word if letter in consonants)


# Видаляємо слова з непарною кількістю приголосних літер
for word in words:
    if count_consonants(word) % 2 != 0:
        text = text.replace(word, "")

print(text)
