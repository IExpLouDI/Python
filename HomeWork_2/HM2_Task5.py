# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
user_num = 0

while user_num != "Y":
    user_num = input("Введите число от 0 до 9. Что бы завершить ввод, введите Y.\n")

    if user_num.title() == "Y":
        user_num = user_num.title()
        continue

    for i in range(len(my_list[::])):
        if my_list[i] < int(user_num):
            my_list.insert(i, int(user_num))
            break
        if i == (len(my_list[::]) - 1):
            my_list.append(int(user_num))

print(my_list)