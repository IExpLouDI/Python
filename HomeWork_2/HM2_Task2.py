# Для списка реализовать обмен значений соседних
# элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний
# сохранить на своем месте.
# Для заполнения списка элементов
# необходимо использовать функцию input().

user_array = []

while True:
    num = input('Введите число. Если хотите закончить ввод введите Y:\n')
    if num.capitalize() == 'Y':
        break
    else:
        user_array.append(int(num))

print('Ваш список:\n', user_array)

for i in range(1, len(user_array), 2):
    user_array[i], user_array[i - 1] = user_array[i - 1], user_array[i]

print('Список после обмена соседних значений:\n', user_array)
