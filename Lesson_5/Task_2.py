# 2. Создать текстовый файл
# (не программно), сохранить в нем
# несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.
string = []
file = open('Task_2.txt', 'r')
string = [line.split() for line in file]
print(string)
number_string = 0
for i in range(len(string)):
    number_string += 1
    number_word = 0
    for j in range(len(string[i])):
        number_word += 1
    print(f"Строка {number_string} количество слов в строке = {number_word} ")
file.close()