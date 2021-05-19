# # Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rest_f = open('text_4_1.txt', 'w', encoding='utf-8')
my_f = open('text_4.txt', 'r', encoding='utf-8')
translate = ["Один", "Два", "Три", "Четыре"]
my_ar = [el.split() for el in my_f.readlines()]

for i in range(len(my_ar)):
    my_ar[i][0] = translate[i]
    rest_f.write(' '.join(my_ar[i]) + '\n')

my_f.close()
rest_f.close()
