# Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func1(a, b):
    try:

        a = int(a)
        b = int(b)

        return a ** b
    except Exception as err:
        return f'{err}'


def my_func2(a, b):
    try:
        a = int(a)
        b = int(b)
        mult = a

        if b > 0:
            for i in range(b - 1):
                mult *= a
            return mult

        elif b < 0:
            for i in range(abs(b) - 1):
                mult *= a
            return 1 / mult

        elif b == 0:
            return 1

    except Exception as err:
        return f'{err}'


var_1 = input("Введите число: ")
var_2 = input("Введите отрицательное число: ")

var_3 = my_func1(var_1, var_2)
var_4 = my_func2(var_1, var_2)

print(f"Первым способом: {var_3}.\n Вторым способом: {var_4}.")
