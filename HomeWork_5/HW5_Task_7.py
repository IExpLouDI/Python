# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
my_dict = {}
my_dict_2 = {}
with open('text_7.txt', encoding='utf-8') as my_f:
    my_arr = [line.split() for line in my_f]
    av_prof = 0
    count = 0
    for el in my_arr:
        my_dict[el[0]] = int(el[2]) - int(el[3])
        if int(el[2]) - int(el[3]) < 0:
            continue
        else:
            av_prof += int(el[2]) - int(el[3])
            count += 1
    my_dict_2['average_profit'] = av_prof / count
    a = [my_dict, my_dict_2]
    with open('text_7_1.json', 'w', encoding='utf-8') as my_js:
        json.dump(a, my_js, indent=4, ensure_ascii=False)