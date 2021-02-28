# 7. Создать (не программно) текстовый файл, в котором
# каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json
spisok = open('Task_7.txt', 'r')
table = [line.split() for line in spisok]
rating = []
dictionary = {}
dictionary_1 = {}
dictionary_2 = {}
sum = 0
count = 0
for i in range(len(table)):
    if int(table[i][2]) > int(table[i][3]):
        dictionary[table[i][0]] = int(table[i][2]) - int(table[i][3])
        sum += int(table[i][2]) - int(table[i][3])
        count += 1
    else:
        dictionary_1[table[i][0]] = int(table[i][3]) - int(table[i][2])
dictionary_2["average_profit"] = sum / count
rating = [dictionary, dictionary_2, dictionary_1]
with open('Task_7.json', "w") as my_file:
    json.dump(rating, my_file)
spisok.close()
