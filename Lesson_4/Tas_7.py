# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
def generator(x):
    step = 1
    for el in count(step):
        if el > x:
            break
        yield el
user_num = int(input("Факториал какого числа хотите вычеслить?\n"))
spisok = []
sum = 1
for i in generator(user_num):
    sum = sum * i
    spisok.append(i)
print(f"{user_num}! = {' * '.join([str(i) for i in spisok])} = {sum}")