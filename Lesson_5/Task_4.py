# Создать (не программно) текстовый файл
# с следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
text_1 = open('Task_4_1.txt', 'r')
text_2 = open('Task_4_2.txt', 'w')
table = [line.split() for line in text_1]
translate_box = ["Один", "Два", "Три", "Четыре"]
for i in range(len(table)):
    string = ""
    table[i][0] = translate_box[i]
    string = ' '.join(table[i])
    text_2.write(string + "\n")
text_1.close()
text_2.close()
