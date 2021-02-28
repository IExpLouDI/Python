# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.
from random import randint
numbers = open('Task_5.txt', 'w')
for i in range(20):
    numbers.write(str(randint(0, 100)) + " ")
numbers.close()
with open('Task_5.txt') as fill:
    line = fill.read().split()
    print(line)
    sum = 0
    for i in range(len(line)):
        sum += int(line[i])
    print(f"Сумма чисел в списке = {sum}")