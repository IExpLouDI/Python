# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_f = open('text_2.txt', 'r')

memory = my_f.read()
my_ar = [el for el in enumerate(memory.split('\n'))]

for el in my_ar:
    print(f"Строка  {el[0] + 1}. Количество слов в строке: {len(el[1])}.")
print(f'Количество строк: {len(my_ar)}.')


my_f.close()
