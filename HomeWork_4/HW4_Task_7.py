# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24

def fact(number):
    for score in range(1, number + 1):
        yield score


my_sum = 1

try:
    num = int(input('Введите число для вычисления факториала: '))
    for i in fact(num):
        my_sum *= i
    print(f"Факториал !{num} = {my_sum}")
except Exception as err:
    print(f"Хьюстон, у нас проблема {err}")
