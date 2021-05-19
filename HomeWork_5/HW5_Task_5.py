# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint
my_f = open('text_5.txt', 'w+', encoding='utf-8')
ar_gen = [randint(0, 20) for i in range(randint(0, 30))]
for i in range(len(ar_gen)):
    my_f.write(str(ar_gen[i]) + ' ')
my_f.seek(0)
my_arr = my_f.read()
s = 0
for el in my_arr.split():
    s += int(el)
print(s)
my_f.close()
