# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def sum_in_string(array):
    array = list(array)
    array_1 = " "
    sum = 0
    for i in range(len(array)):
        if ord(array[i]) >= 48 and ord(array[i]) <= 57 or ord(array[i]) == 32:
            array_1 += array[i]
    array_1 = array_1.split()
    for i in range(len(array_1)):
        sum += int(array_1[i])
    return sum
with open('Task_6.txt') as note:
    line = [line.split() for line in note]
    dictionary = {}
    for i in range(len(line)):
        dictionary[line[i][0]] = sum_in_string(' '.join(line[i]))
    print(dictionary)
