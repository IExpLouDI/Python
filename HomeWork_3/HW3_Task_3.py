# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func():

    my_array = []
    size = 3

    for i in range(size):
        try:
            my_array.append(int(input(f'Введите {i + 1}-e число: ')))
        except Exception as err:
            return err

    return sum(sorted(my_array)[1::])


c = my_func()

print(f'Сумма наибольших двух чисел = {c}.')
