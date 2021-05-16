# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_f = open('text_1.txt', 'w')
while True:
    user_string = input("Enter your string:\n")
    my_f.writelines(user_string + '\n')
    if user_string == '':
        break

my_f.close()
