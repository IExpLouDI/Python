# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ
# — характеристика товара, например, название. Тогда значение — список значений-характеристик,
# например, список названий товаров.
# # Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }
my_list = []
my_tuple = tuple()
my_dict = dict()
count = 1
memory_list = []
analise_dict = dict()
param = ["Название", "Цена", "Количество", "Ед"]
user_answer = 0

while user_answer != "Y":
    my_dict = dict()
    for el in param:
        if el == 'цена' or el == 'количество':
            user_answer = int(input(f"{el}: "))
            my_dict[el] = user_answer
        else:
            user_answer = input(f"{el}: ")
            my_dict[el] = user_answer

    my_tuple = (count, my_dict)
    my_list.append(my_tuple)
    count += 1
    user_answer = input("Закончить ввод? Y/N: ").title()[0]
    if user_answer != "Y" and user_answer != "N":
        while True:
            user_answer = input("Закончить ввод? Y/N: ").title()
            if user_answer[0] == "Y" or user_answer[0] == "N":
                break

for el in param:
    memory_list = []
    for i in range(len(my_list)):
        memory_list.append(my_list[i][1][el])
    if el == 'Ед':
        memory_list = list(set(memory_list))
    analise_dict[el] = memory_list

print("Результат аналитики о товарах:\n", analise_dict)
