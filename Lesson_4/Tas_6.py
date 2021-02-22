# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.

from itertools import cycle, count

usernum = int(input("С какого положительного числа начать генерацию? \n"))
user_count = int(input("Сколько чисел нужно сгенерировать?\n"))
user_str = input("Введите набор слов:\n").split()
step = 0

for word in cycle(user_str):
    if step > 5:
        break
    print(word)
    step += 1

for x in count(usernum):
    if x > usernum + user_count:
        break
    print(x)
