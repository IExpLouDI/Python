# Пользователь вводит строку
# из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное,
# выводить только первые 10 букв в слове.

user_word = input("Введите всё что угодно!\n")
user_array = user_word.split()

for i in range(len(user_array)):
    print(f"{i + 1} слово - {user_array[i][:10]}")